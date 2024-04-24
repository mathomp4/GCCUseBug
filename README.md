# GCC Use Issue Reproducer

## Requirements

To run this reproducer you will need:

- A Fortran compiler (e.g. `gfortran`)
- Python 3
- Jinja2 (Python package)
- CMake 3.20 or newer

## Creating a reproducible test case

To create a reproducible test case, use the `create_reproducer.py` script:
```bash
$ ./create_reproducer.py -h
usage: create_reproducer.py [-h] [--max-modules MAX_MODULES] [--num-subs NUM_SUBS]

Create Fortran modules for testing

options:
  -h, --help            show this help message and exit
  --max-modules MAX_MODULES
                        Maximum number of modules to create (must be a multiple of 10) (default: 100)
  --num-subs NUM_SUBS   Number of subroutines per module (default: 10)
```

As can be seen it has two options:
- `--max-modules`: Maximum number of modules to create (must be a multiple of 10)
- `--num-subs`: Number of subroutines per module

The script will create a directory with the following structure:
```
Modules_{max-modules}-Subs_{num-subs}/
```

In that directory will be a series of directories:
```
Modules_10
Modules_20
...
Modules_{max-modules}
```
and a `build.sh` script that builds and will output the timings. These will be on screen
and in a file called `build_times.txt`


