import os
import ext.data
import ext.win

# Get Current Directory
current_dir = os.getcwd()

# Create the categorizer folder in current directory
os.mkdir(current_dir + "CATEGORIZER")

# Go to this directory
current_dir = current_dir + "CATEGORIZER"

# List all elements in directory
file_list: list = ext.win.list_files(current_dir)

print(current_dir, file_list)