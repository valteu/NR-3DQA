import os
import numpy as np
import open3d as o3d

# Set the directory path where your point clouds are stored
directory_path = 'pointclouds'

# Get a list of all files in the directory
file_list = os.listdir(directory_path)

# Iterate over each file
for filename in file_list:
    if filename.endswith('.ply'):
        # Load the point cloud
        point_cloud = o3d.io.read_point_cloud(os.path.join(directory_path, filename))

        # Apply your statistical outlier removal method here (e.g., using Isolation Forest or PyOD)

        # Save the cleaned point cloud with the new filename
        new_filename = filename.replace('.ply', '_post.ply')
        o3d.io.write_point_cloud(os.path.join(directory_path, new_filename), point_cloud)

        print(f"Saved cleaned point cloud as {new_filename}")

print("Processing complete!")
