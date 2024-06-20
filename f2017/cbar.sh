#!/bin/bash

# Check if an argument is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <path_to_cpp_file>"
    exit 1
fi

input_file="$1"
# Extract the base name without the extension
base_name="${input_file%.*}"

# Compile the C++ file
clang++ -std=c++17 -o "${base_name}.build" "$input_file" 2>&1

# Check if compilation was successful
if [ $? -eq 0 ]; then
    # Execute the compiled program
    ./"${base_name}.build"
else
    echo "Compilation failed."
    exit 1
fi
