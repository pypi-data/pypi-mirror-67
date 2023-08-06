
import sys

import whatifmachine

def main():
    import argparse
    import os
    parser = argparse.ArgumentParser(description="Profile a script or module")
    parser.add_argument("-a", "--auto", action="store_true", help="autoprofile the whatifs")
    parser.add_argument("-o", "--outfile", help="save stats to <outfile>")
    parser.add_argument("-f", "--filter", default=[], action="append", help="filter stats")
    parser.add_argument("-s", "--sort", help="Sort order when printing to stdout, based on pstats.Stats class", default="stdname")
    parser.add_argument("-m", "--module", action="store_true", help="Specified script is a module")
    parser.add_argument("script", help="Script to run")
    parser.add_argument("args", nargs="*", help="Arguments to script")
    args = parser.parse_args()

    sys.argv = [args.script] + args.args  # Reset sys.argv to the caller.

    prof = whatifmachine.Profile()
    if args.module:
        import runpy
        code = "run_module(modname, run_name='__main__')"
        globs = {"run_module": runpy.run_module, "modname": args.module, "whatif": prof.whatif}
    else:
        sys.path.insert(0, os.path.dirname(args.script))
        with open(args.script, "rb") as fp:
            code = compile(fp.read(), args.script, "exec")
        globs = {"__file__": args.script, "__name__": "__main__", "__package__": None, "__cached__": None, "whatif": prof.whatif}

    if args.auto:
        prof.master_distort = lambda t: 100.0 / 100.0 * t
        prof.runctx(code, globs, None)
        full_time = prof.total_time
        print('100%: {:.3f}s (100%)'.format(full_time))
        for scale in reversed(range(0, 100, 10)):
            prof.__init__()
            prof.master_distort = lambda t: scale / 100.0 * t
            prof.runctx(code, globs, None)
            print('{:3}%: {:.3f}s ({:.0f}%)'.format(scale, prof.total_time, 100 * prof.total_time / full_time))
    elif args.outfile:
        prof.runctx(code, globs, None)
        if args.outfile is not None:
            prof.dump_stats(args.outfile)
    else:
        prof.runctx(code, globs, None)
        prof.print_stats(*args.filter, sort=args.sort)

if __name__ == '__main__':
    main()

