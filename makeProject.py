import os
import subprocess
import shutil

directory_path = "."

# Get a list of all entries (files and directories) in the specified directory
entries = os.listdir(directory_path)

# Initialize empty lists to store directories and files
directories = []
files = []

# Separate entries into directories and files
for entry in entries:
    full_path = os.path.join(directory_path, entry)
    if os.path.isdir(full_path):
        directories.append(entry)
    else:
        files.append(entry)

# Remove files containing "rampage-r" in their full names
for file in files:
    if "rampage-r" in file:
        os.remove(file)

# Get revision number using git
revision_number = subprocess.check_output(["git", "rev-list", "--count", "HEAD"]).decode().strip()

# Define file names
filename_base = "rampage-stats-r" + revision_number
zip_name = filename_base + ".zip"
pk3_name = filename_base + ".pk3"

print("Compiling pk3, this may take 10-20 seconds...")

# Compress files into a zip archive
shutil.make_archive(filename_base, 'zip', "pk3")

# Check if the zip archive exists
if not os.path.exists(zip_name):
    print("Unable to zip up directory")
    exit(1)

# Rename the zip archive to pk3
os.rename(zip_name, pk3_name)

# Check if pk3 file exists
if os.path.exists(pk3_name):
    print("Finished compilation!")
else:
    print("Compilation failed to rename the .zip to a .pk3")
    exit(1)