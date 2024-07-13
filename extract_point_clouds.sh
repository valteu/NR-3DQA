#!/bin/bash

# Create the pointclouds directory if it doesn't exist
mkdir -p ./pointclouds

# Find all input.ply files and copy them to the pointclouds directory
find ./output_dhc -type f -name "input.ply" -exec sh -c '
    # Get the full path of the input.ply file
    input_ply="$1"
    
    # Extract the directory name (origin directory)
    origin_dir=$(dirname "$input_ply")
    
    # Remove the leading "./datasets" from the origin directory
    relative_dir=${origin_dir#./output_dhc/}
    
    # Construct the target path in the pointclouds directory
    target_path="./pointclouds/${relative_dir}_old_input.ply"
    
    # Copy the input.ply file to the target path
    cp "$input_ply" "$target_path"
' sh {} \;
