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

def main():
    # Our templates will be in templates/ directory
    templateLoader = jinja2.FileSystemLoader(searchpath="./templates")

    # We will use the default template environment
    templateEnv = jinja2.Environment(loader=templateLoader)

    # As a test we will create 10 modules
    # We will first template the file:
    #  base_template.F90
    # which is just a jinja loop of USE statements
    base_template = templateEnv.get_template("base_template.F90")
    # It expects a variable called "num_modules" which is the number of modules
    # to create

    # We will create 10 modules
    num_modules = 10

    # Next create a directory called Modules_10 where we will store the 
    # created modules. The last number is based on the number of modules
    # we are creating

    # Create the directory
    os.makedirs("Modules_{}".format(num_modules))

    # Now we will template our file and put the result in the directory
    with open("Modules_{}/base.F90".format(num_modules), "w") as f:
        f.write(base_template.render(num_modules=num_modules))



if __name__ == '__main__':
    main()