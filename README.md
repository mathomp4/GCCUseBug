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
usage: create_reproducer.py [-h] [--max-modules MAX_MODULES] [--num-subs NUM_SUBS] [--random-names]

Create Fortran modules for testing

options:
  -h, --help            show this help message and exit
  --max-modules MAX_MODULES
                        Maximum number of modules to create (must be a multiple of 10) (default: 50)
  --num-subs NUM_SUBS   Number of subroutines per module (default: 10)
  --random-names        Use random module names (default: False)
```

As can be seen it has three options:
- `--max-modules`: Maximum number of modules to create (must be a multiple of 10)
- `--num-subs`: Number of subroutines per module
- `--random-names`: Use random module names

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

## Results

### IFX 2024.1

| Num Mods in base.F90 | 200 Mods/Mod | 500 Mods/Mod | 1000 Mods/Mod |
|----------------------|--------------|--------------|---------------|
| 10                   | 0.0566994    | 0.0730116    | 0.100479      |
| 20                   | 0.0687903    | 0.100407     | 0.15462       |
| 30                   | 0.0797278    | 0.127941     | 0.209833      |
| 40                   | 0.0913473    | 0.171004     | 0.259712      |
| 50                   | 0.103962     | 0.18284      | 0.314469      |

### GCC 13.2.0

| Num Mods in base.F90 | 200 Mods/Mod | 500 Mods/Mod | 1000 Mods/Mod |
|----------------------|--------------|--------------|---------------|
| 10                   | 0.126971     | 0.505483     | 1.55647       |
| 20                   | 0.340988     | 1.75751      | 6.41986       |
| 30                   | 0.734456     | 3.755        | 12.7215       |
| 40                   | 1.16991      | 6.747        | 25.4188       |
| 50                   | 1.78235      | 9.8174       | 36.3083       |
