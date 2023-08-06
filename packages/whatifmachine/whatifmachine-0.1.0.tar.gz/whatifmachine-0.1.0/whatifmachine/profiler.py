#! /usr/bin/env python3

""" Class for profiling Python code. """

# See:
#   https://docs.python.org/3/library/profile.html#module-profile
#   https://docs.python.org/3/library/sys.html#sys.setprofile
#   https://github.com/python/cpython/blob/3.8/Lib/profile.py
#   https://github.com/rkern/line_profiler/blob/master/kernprof.py#L110

# Inspired by the profile module by James Roskind...
#   which was based on a profiler by Sjoerd Mullender...
#     which was hacked somewhat by Guido van Rossum.

from collections import defaultdict
from functools import wraps
from time import process_time as get_time
import marshal
import pstats
import sys

import attr


@attr.s(slots=True)
class Entry:
    """ Record all of the information about an active stack frame. """
    name = attr.ib(default=0)  # Name of the function corresponding to this frame.
    frame = attr.ib(default=None)  # The corresponding frame, this is only used in sanity checks.
    distort = attr.ib(default=lambda x: x)  # How to distort time in this entry.
    internal_time = attr.ib(default=0)  # Total time spent in this frame's function, excluding time in sub-functions.
    external_time = attr.ib(default=0)  # Total time spent in sub-functions, excluding time executing the frame's function.


@attr.s(slots=True)
class Timings:
    """ Record all of the information about the calls to a single function. """
    call_count = attr.ib(default=0)  # The number of times this function was called, not counting direct or indirect recursion.
    running_time = attr.ib(default=0)  # Total time that this function was on top of the stack.
    stack_time = attr.ib(default=0)  # Total time that this function was present on the stack.
    callers = attr.ib(factory=lambda: defaultdict(int))  # A dictionary indicating for each function name, the number of times it was called by us.
    stack_count = attr.ib(default=0)  # Number of occurrences of this function currently on the stack.


class Profile:
    """ Profiler class. """

    def __init__(self):
        self.last_time = get_time()
        self.stack = [Entry(("profile", 0, "fake"))]  # Our external "parallel stack" to avoid contaminating the program being profiled, it always contains one fake entry.
        self.timings = defaultdict(Timings)  # Timing data for each function stored under Entry.name.
        self.stats = dict()
        self.master_distort = None
        self.distort = lambda x: x

    @property
    def total_time(self):
        return self.stack[-1].external_time

    def dispatcher(self, frame, event, arg):
        self.stack[-1].internal_time += self.stack[-1].distort(get_time() - self.last_time)  # Log how much (distorted) time has passed since we were last here.

        if event in ("call", "c_call"):  # Push frame.
            assert len(self.stack) == 1 or (frame.f_back if event == "call" else frame) is self.stack[-1].frame  # Sanity.
            name = (frame.f_code.co_filename, frame.f_code.co_firstlineno, frame.f_code.co_name) if event == "call" else ("", 0, arg.__name__)

            self.stack.append(Entry(name, frame, self.distort))
            self.timings[name].stack_count += 1
        else:  # if event in ("return", "c_return", "c_exception"):  # Pop frame.
            assert frame is self.stack[-1].frame  # Sanity.

            current = self.stack.pop()  # Pop.
            previous = self.stack[-1]  # Peek.
            previous.external_time += current.internal_time + current.external_time

            # Collate timing information.
            timings = self.timings[current.name]
            timings.stack_count -= 1
            timings.running_time += current.internal_time
            timings.callers[previous.name] += 1
            if timings.stack_count == 0:  # We have just removed the last occurrence of the current function from the stack.
                # Hence this is not a (direct or indirect) recursive call and so it is finally time to update its cumulative time.
                timings.stack_time += current.internal_time + current.external_time
                timings.call_count += 1

        self.last_time = get_time()

    def whatif(self, distort=lambda x: x, factor=1.0, bias=0.0, maximum=float('inf')):
        """ The whatif(...) decorator. """
        if self.master_distort is None:
            frame_distort = lambda t: distort(factor*min(t, maximum) + bias)
        else:
            frame_distort = self.master_distort

        def wrapper(func):
            @wraps(func)
            def inner(*args, **kwds):
                self.distort, old_distort = frame_distort, self.distort
                try:
                    result = func(*args, **kwds)
                finally:
                    self.distort = old_distort  # Restore old distortion.
                return result
            return inner
        return wrapper

    def runctx(self, cmd, globs, locs):
        """ Profile a command (given as a string) in the context of the given globals and locals. """

        sys.setprofile(self.dispatcher)
        try:
            exec(cmd, globs, locs)
        finally:
            sys.setprofile(None)
        # self.stack now contains the starting fake frame and the "c_call" for self.setprofile since we never saw the corresponding "c_return".
        assert len(self.stack) == 2
        self.dispatcher(self.stack[-1].frame, "return", None)
        assert len(self.stack) == 1

        return self

    def create_stats(self):
        # Needed so that Pstat can be initialised off of this class.
        while len(self.stack) > 1:  # Clear the stack back to the fake frame entry.
            self.dispatcher(self.stack[-1].frame, "return", None)

        self.stats = {
            func: (timings.call_count, sum(timings.callers.values()), timings.running_time, timings.stack_time, timings.callers.copy())
            for func, timings in self.timings.items()
            }

    def print_stats(self, *args, sort="stdname"):
        pstats.Stats(self).sort_stats(sort).print_stats(*args)

    def dump_stats(self, file):
        with open(file, "wb") as f:
            self.create_stats()
            marshal.dump(self.stats, f)

