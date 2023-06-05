import os
import win

# Get Current Directory
current_dir = os.getcwd()
datas: list = []
try:
    # Create the categorizer folder in current directory
    os.mkdir(current_dir + "CATEGORIZER")

    # Create all categorizer init folders in current directory
    datas = win.init_folders()
except FileExistsError:
    pass

# Go to this directory
current_dir = current_dir + "CATEGORIZER"

# List all elements in directory
file_list: list = win.list_files(current_dir)

# Categorize all files with dictionary
categorized_files: dict = win.set_categorize_files(file_list, current_dir)

# Program starts here... no comment more.
for directory_name in datas:
    get_categorized_file_list = categorized_files[directory_name]
    print(get_categorized_file_list)

print(datas)