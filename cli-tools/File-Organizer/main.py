# File Organizer Script
# Sort files by extension
# Create folders automatically

import os
import shutil

folder_path = r"C:\Users\Lenovo\classroom\test_folder"

file_map = {
    ".txt": "Text",
    ".jpg": "Images",
    ".png": "Images",
    ".mp3": "Music",
    ".mp4": "Videos",
    ".pdf": "PDF"
}

print("Scanning folder...\n")

moved_count = 0  # Counter for moved files

for file in os.listdir(folder_path):
    source = os.path.join(folder_path, file)

    # Skip folders
    if not os.path.isfile(source):
        continue

    file_ext = os.path.splitext(file)[1].lower()

    if file_ext in file_map:
        target_folder = os.path.join(folder_path, file_map[file_ext])

        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        destination = os.path.join(target_folder, file)
        shutil.move(source, destination)

        print(f"Moving {file} → {file_map[file_ext]}")
        moved_count += 1  # Increment counter

print(f"\nOrganizing complete! Moved {moved_count} files successfully.")