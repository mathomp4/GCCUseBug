#!/usr/bin/env bash

# This script is used to build our tests. There
# are a series of directories called Modules_N
# where N is a number. Each of these directories
# contains a CMakeLists.txt file that is used to
# build the tests in that directory. 

# This script will loop over all those directories,
# grab the number from the directory name, and then
# build the tests in that directory capturing the build times

# Then we will output the build times to screen in
# a nice table format

for i in $(ls -d Modules_* | sort -V); do
    # Get the number from the directory name
    num=$(echo $i | sed 's/Modules_//')
    # Run cmake
    echo "Running cmake in $i"
    cmake -S $i -B $i/build -DCMAKE_BUILD_TYPE=Debug --fresh > /dev/null 2>&1
    # Build the tests
    echo "Building in $i"
    # Capture the build time into a file in the Modules_N directory
    # NOTE: We are using --parallel here to take advantage of the
    #       fact that the modules other than base do not depend on
    #       each other. But if you are having issues you can change
    #       the number of jobs here by either doing "--parallel 8"
    #       say, or setting CMAKE_BUILD_PARALLEL_LEVEL=8 in the environment
    cmake --build --parallel $i/build > $i/build_time.txt 2>&1

    # In the build_time.txt file, the second to last line
    # contains the build time:
    # Elapsed time (seconds): 0.0493425
    # We can use tail to get the second to last line
    # and then use awk to get the build time and store it
    # in a dictionary based on the number of the module
    time=$(tail -2 $i/build_time.txt | head -1 | awk '{print $4}')
    echo "Build time for base.F90 in $i: $time seconds"
    time_dict[$num]=$time

done

# Now we want to output the build times in a nice table format both to screen
# and to a file
echo "Number of Modules | Build Time"
echo "----------------- | ----------"
echo "Number of Modules | Build Time" > build_times.txt
echo "----------------- | ----------" >> build_times.txt
for key in ${!time_dict[@]}; do
    printf "%17s | %10s\n" $key ${time_dict[$key]}
    printf "%17s | %10s\n" $key ${time_dict[$key]} >> build_times.txt
done
