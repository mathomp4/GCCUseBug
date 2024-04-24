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
                        Maximum number of modules to create (must be a multiple of 10) (default: 50)
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

## Results

### IFX 2024.1

| Num Mods in base.F90 | 10 Mods/Mod | 20 Mods/Mod | 50 Mods/Mod | 100 Mods/Mod | 200 Mods/Mod |
|----------------------|-------------|-------------|-------------|--------------|--------------|
| 10                   | 0.0479359   | 0.0513784   | 0.060279    | 0.0754805    | 0.105457     |
| 20                   | 0.058456    | 0.0688587   | 0.103876    | 0.159299     | 0.270871     |
| 30                   | 0.0716657   | 0.0975519   | 0.172865    | 0.296027     | 0.532619     |
| 40                   | 0.0923233   | 0.137277    | 0.268651    | 0.479169     | 0.905834     |
| 50                   | 0.115967    | 0.185385    | 0.384408    | 0.714401     | 1.37546      |

### GCC 13.2.0

| Num Mods in base.F90 | 10 Mods/Mod | 20 Mods/Mod | 50 Mods/Mod | 100 Mods/Mod | 200 Mods/Mod |
|----------------------|-------------|-------------|-------------|--------------|--------------|
| 10                   | 0.0235352   | 0.0301774   | 0.054383    | 0.110551     | 0.336674     |
| 20                   | 0.0393153   | 0.0644458   | 0.19694     | 0.637871     | 2.34525      |
| 30                   | 0.0647286   | 0.134374    | 0.530658    | 1.9606       | 7.37042      |
| 40                   | 0.103963    | 0.238685    | 1.23998     | 4.78349      | 17.2896      |
| 50                   | 0.154701    | 0.379783    | 2.32        | 8.61682      | 33.9653      |
