"""Execute files of Python code."""

import imp
import os
import sys
import tokenize
import mimetypes
from xdis import load_module, PYTHON_VERSION

SUPPORTED_PYTHON_VERSIONS = (2.5, 2.6, 2.7, 3.3, 3.2, 3.4, 3.5)

from xpython.pyvm2 import VirtualMachine


# This code is ripped off from coverage.py.  Define things it expects.
try:
    open_source = tokenize.open  # pylint: disable=E1101
except:

    def open_source(fname):
        """Open a source file the best way."""
        return open(fname, "rU")


CannotCompile = WrongBytecode = NoSource = Exception


def exec_code_object(code, env, python_version=PYTHON_VERSION):
    vm = VirtualMachine(python_version)
    vm.run_code(code, f_globals=env)


# from coverage.py:

try:
    # In Py 2.x, the builtins were in __builtin__
    BUILTINS = sys.modules["__builtin__"]
except KeyError:
    # In Py 3.x, they're in builtins
    BUILTINS = sys.modules["builtins"]


def rsplit1(s, sep):
    """The same as s.rsplit(sep, 1), but works in 2.3"""
    parts = s.split(sep)
    return sep.join(parts[:-1]), parts[-1]


def run_python_module(modulename, args):
    """Run a python module, as though with ``python -m name args...``.

    `modulename` is the name of the module, possibly a dot-separated name.
    `args` is the argument array to present as sys.argv, including the first
    element naming the module being executed.

    """
    openfile = None
    glo, loc = globals(), locals()
    try:
        try:
            # Search for the module - inside its parent package, if any - using
            # standard import mechanics.
            if "." in modulename:
                packagename, name = rsplit1(modulename, ".")
                package = __import__(packagename, glo, loc, ["__path__"])
                searchpath = package.__path__
            else:
                packagename, name = None, modulename
                searchpath = None  # "top-level search" in imp.find_module()
            openfile, pathname, _ = imp.find_module(name, searchpath)

            # Complain if this is a magic non-file module.
            if openfile is None and pathname is None:
                raise NoSource("module does not live in a file: %r" % modulename)

            # If `modulename` is actually a package, not a mere module, then we
            # pretend to be Python 2.7 and try running its __main__.py script.
            if openfile is None:
                packagename = modulename
                name = "__main__"
                package = __import__(packagename, glo, loc, ["__path__"])
                searchpath = package.__path__
                openfile, pathname, _ = imp.find_module(name, searchpath)
        except ImportError:
            _, err, _ = sys.exc_info()
            raise NoSource(str(err))
    finally:
        if openfile:
            openfile.close()

    # Finally, hand the file off to run_python_file for execution.
    args[0] = pathname
    run_python_file(pathname, args, package=packagename)


def run_python_file(filename, args, package=None):
    """Run a python file as if it were the main program on the command line.

    `filename` is the path to the file to execute, it need not be a .py file.
    `args` is the argument array to present as sys.argv, including the first
    element naming the file being executed.  `package` is the name of the
    enclosing package, if any.

    """
    # Create a module to serve as __main__
    old_main_mod = sys.modules["__main__"]
    main_mod = imp.new_module("__main__")
    sys.modules["__main__"] = main_mod
    main_mod.__file__ = filename
    if package:
        main_mod.__package__ = package
    main_mod.__builtins__ = BUILTINS

    # Set sys.argv and the first path element properly.
    old_argv = sys.argv
    old_path0 = sys.path[0]
    sys.argv = args
    if package:
        sys.path[0] = ""
    else:
        sys.path[0] = os.path.abspath(os.path.dirname(filename))

    try:
        # Open the source or bytecode file.
        try:
            mime = mimetypes.guess_type(filename)
            if mime == ("application/x-python-code", None):
                (
                    python_version,
                    timestamp,
                    magic_int,
                    code,
                    pypy,
                    source_size,
                    sip_hash,
                ) = load_module(filename)
                if python_version not in SUPPORTED_PYTHON_VERSIONS:
                    raise WrongBytecode(
                        "We only support bytecode 2.5 - 2.7 and 3.2 - 3.5: %r is %2.1f bytecode"
                        % (filename, python_version)
                    )
                pass
            else:
                source_file = open_source(filename)
                try:
                    source = source_file.read()
                finally:
                    source_file.close()

                if PYTHON_VERSION not in SUPPORTED_PYTHON_VERSIONS:
                    raise CannotCompile(
                        "We need Python 2.5 - 2.7 or 3.2 - 3.5 to compile source code; you are running Python %s"
                        % PYTHON_VERSION
                    )

                # We have the source.  `compile` still needs the last line to be clean,
                # so make sure it is, then compile a code object from it.
                if not source or source[-1] != "\n":
                    source += "\n"
                code = compile(source, filename, "exec")
                python_version = PYTHON_VERSION

        except IOError:
            raise NoSource("No file to run: %r" % filename)

        # Execute the source file.
        exec_code_object(code, main_mod.__dict__, python_version)

    finally:
        # Restore the old __main__
        sys.modules["__main__"] = old_main_mod

        # Restore the old argv and path
        sys.argv = old_argv
        sys.path[0] = old_path0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: execfile.py <filename> args")
        os.exit(1)
    run_python_file(sys.argv[1], sys.argv[2:])
