import os
import shutil

# Source and destination folders
source_folder = "source_images"
destination_folder = "moved_images"

# Create destination folder if it does not exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Loop through files in source folder
for file in os.listdir(source_folder):

    # Check if file is jpg
    if file.endswith(".jpg"):

        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)

        shutil.move(source_path, destination_path)

        print(f"{file} moved successfully!")

print("All JPG files moved.")