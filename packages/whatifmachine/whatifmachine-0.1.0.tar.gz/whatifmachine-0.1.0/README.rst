
WhatIfMachine
=============

The WhatIfMachine is a Python profiler which allows you to see what would happen to a profile if its functions ran in different amounts of time.

It officially supports 3.6 -- 3.8.

Quickstart
----------

Get the WhatIfMachine from `PyPI`_::

    $ pip install whatifmachine --user --upgrade

Use it to profile a script with arguments::

    $ whatifmachine script.py arg1 arg2 arg3

Fullstart
---------

Here's a little script ``test.py``::

    def f(n):
        for i in range(5):
            h(n)
            try:
                g(i + n)
            except ValueError:
                pass

    def g(n, k=100_000):
        n = h(n, k)
        if n < 10**30106:
            raise ValueError('n is too small')
        return n

    def h(n, k=100_000):
        for _ in range(k):
            n = 2 * n
        return n

    f(1000)

We can profile this using the WhatIfMachine::

    $ whatifmachine -f test test.py
             19 function calls in 4.189 seconds

       Ordered by: standard name
       List reduced from 6 to 4 due to restriction <'test'>

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            5    0.011    0.002    2.112    0.422 test.py:11(g)
           10    4.178    0.418    4.178    0.418 test.py:17(h)
            1    0.000    0.000    4.189    4.189 test.py:2(<module>)
            1    0.000    0.000    4.189    4.189 test.py:2(f)

Note that we use the ``-f test`` option to filter the output to only show lines matching ``test``.

But WhatIfMachine provides the ``whatif(...)`` decorator, which can be used to change how a function appears when profiled.
For example, we can add the decorator with the ``factor=0.5`` argument to ``g``::

    @whatif(factor=0.5)
    def g(n, k=100_000):
        n = h(n, k)
        if n < 10**30106:
            raise ValueError('n is too small')
        return n

This allows us to see what the impact would be if ``g`` only took half the time to run::

    $ whatifmachine -f test test.py
             41 function calls in 3.049 seconds

       Ordered by: standard name
       List reduced from 14 to 4 due to restriction <'test'>

       ncalls  tottime  percall  cumtime  percall filename:lineno(function)
            5    0.004    0.001    1.030    0.206 test.py:10(g)
           10    3.044    0.304    3.044    0.304 test.py:17(h)
            1    0.000    0.000    3.049    3.049 test.py:2(<module>)
            1    0.000    0.000    3.049    3.049 test.py:2(f)

So we can see that making ``g`` 100% faster would only make the script 37% faster.
By comparison, the WhatIfMachine allows us to discover that the same effect can be achieved by making ``h`` just 40% faster.

This is the impact of `Amdahl's law <https://en.wikipedia.org/wiki/Amdahl%27s_law>`_.
So although the WhatIfMachine can't actually make your code run any faster, it can indicate where investing your effort in optimising your code can have the biggest payoff.

Decorator
---------

The WhatIfMachine's ``whatif`` decorator can be given any function that maps floats to floats, for example ``@whatif(lambda x: x*x)``.
Before this it also applies (in order):

 - a maximum amount of time that the call would take (``@whatif(maximum=0.1)``)
 - a multiplicative factor (``@whatif(factor=0.9)``)
 - an additive bias (``@whatif(bias=-0.05)``)

These can be combined.
For example, suppose a function is decorated with ``@whatif(abs, factor=2, bias=-0.1)``.
Then the WhatIfMachine reports ``t`` seconds passing within this function as ``abs(2*t - 0.1)`` seconds, whatever use that is.

Be careful, there is nothing to stop you from distorting time in a way which results in functions appearing to take zero or even a negative amount of time to run.
Good luck understanding those profile reports.

External Links
--------------

* `PyPI`_
* `GitHub`_

.. _GitHub: https://github.com/MarkCBell/whatifmachine
.. _PyPI: https://pypi.org/project/whatifmachine

