#!/usr/bin/env python3

"""This script creates a series of Fortran modules to test a bug in GCC"""


# What does this do. We need to do the following:

# We are trying to replicate a bug in gfortran wherein if you have say 50 to 100
# modules and a single file called base.F90 that is just a collection of USE
# statements, the compilation time increases. Maybe O(n) or O(n^2)

# So we will use jinja2 to create a series of modules with random names and a
# base.F90 file that just has a collection of USE statements. We will then
# compile the modules and then base.F90 file and see how long it takes

import jinja2
import os
import shutil

# We will use argparse to add commandline arguments for
# 1. Number of module directories to create (must be a multiple of 10)
# 2. Number of subroutines per module (default is 10)

def parse_args():
    import argparse
    parser = argparse.ArgumentParser(description="Create Fortran modules for testing",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--max-modules",
                        type=int,
                        default=100,
                        help="Maximum number of modules to create (must be a multiple of 10)")
    parser.add_argument("--num-subs",
                        type=int,
                        default=10,
                        help="Number of subroutines per module")
    return parser.parse_args()

def main():

    args = parse_args()
    max_number_of_modules = args.max_modules
    # max_number_of_modules must be a multiple of 10
    if max_number_of_modules % 10 != 0:
        raise ValueError("max-modules must be a multiple of 10")
    number_of_subroutines_per_module = args.num_subs

    # Our templates will be in templates/ directory
    templateLoader = jinja2.FileSystemLoader(searchpath="./templates")

    # We will use the default template environment
    templateEnv = jinja2.Environment(loader=templateLoader)

    # We will first template the file:
    #  base_template.F90
    # which is just a jinja loop of USE statements
    base_template = templateEnv.get_template("base_template.F90")
    # It expects a variable called "num_modules" which is the number of modules
    # to create

    # Now we create a directory called:
    #   Modules_(max_number_of_modules)-Subs_(number_of_subroutines_per_module)
    # where we will store the created modules
    overall_directory = "Modules_{}-Subs_{}".format(max_number_of_modules, number_of_subroutines_per_module)
    # If the directory already exists, we will delete it
    if os.path.exists(overall_directory):
        shutil.rmtree(overall_directory)
    os.makedirs(overall_directory)

    # Next we copy other/build.sh to the overall directory
    shutil.copy("other/build.sh", overall_directory)

    # We will use a loop to create the modules
    for num_modules in range(10, max_number_of_modules+10, 10):

        # Next create a directory called Modules_10 where we will store the 
        # created modules. The last number is based on the number of modules
        # we are creating

        # Create the directory under the overall directory
        os.makedirs("{}/Modules_{}".format(overall_directory, num_modules))

        # Now we will template our file and put the result in the directory
        with open("{}/Modules_{}/base.F90".format(overall_directory, num_modules), "w") as f:
            f.write(base_template.render(num_modules=num_modules))

        # We also have a module template that we will use to create the modules
        module_template = templateEnv.get_template("module_template.F90")

        # Now we will create the modules using Fortran numbering, starting from 1
        for i in range(1, num_modules+1):
            with open("{}/Modules_{}/module{}.F90".format(overall_directory, num_modules, i), "w") as f:
                f.write(module_template.render(n=i,num_subs=number_of_subroutines_per_module))

        # Now we template the CMakelists.txt file using the template
        #  templates/CMakelists_template.txt
        # and put it in our Modules_N directory
        cmake_template = templateEnv.get_template("CMakelists_template.txt")
        with open("{}/Modules_{}/CMakeLists.txt".format(overall_directory, num_modules), "w") as f:
            f.write(cmake_template.render(num_modules=num_modules))

if __name__ == '__main__':
    main()
