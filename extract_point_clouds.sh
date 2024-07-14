#!/bin/bash

# Create the pointclouds directory if it doesn't exist
mkdir -p ./pointclouds

# variable containing path
path="./output_dhc"

# Find all input.ply files and copy them to the pointclouds directory
find $path -type f -name "input.ply" -exec sh -c '
    input_ply="$1"
    origin_dir=$(dirname "$input_ply")
    relative_dir=${origin_dir#$path}
    target_path="./pointclouds/${relative_dir}_old_input.ply"
    
    # Copy the input.ply file to the target path
    cp "$input_ply" "$target_path"
' sh {} \;
