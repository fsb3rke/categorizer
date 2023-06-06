import os
import win
import time

# Get Current Directory
current_dir = os.getcwd()

try:
    # Create the categorizer folder in current directory
    os.mkdir(os.path.join(current_dir, "CATEGORIZED"))
except FileExistsError:
    pass

# Go to this directory
categorizer_dir = os.path.join(current_dir, "CATEGORIZED")

# Create the categorizer init folder in CATEGORIZER folder
os.chdir(categorizer_dir)
datas: list = win.init_folders()
os.chdir(current_dir)

# List all elements in directory
file_list: list = win.list_files(current_dir)

# Categorize all files with dictionary
categorized_files: dict = win.set_categorize_files(file_list, current_dir)

# Program starts here... no comment more.
for directory_name in datas:
    categorized_file_list: list = categorized_files[directory_name]
    if categorized_file_list is []:
        continue

    for file in categorized_file_list:
        file_name_n_ext = file.split('\\')[-1]
        win.move_file_to_directories(file_path=file, move_path=os.path.join(categorizer_dir, f"{directory_name}\\{file_name_n_ext}"))
        print(f"FILE({file_name_n_ext}) MOVED {current_dir}\n\t\tTO {os.path.join(categorizer_dir, directory_name)}", end="\n\n")

# print(datas)

print("Thanks for using categorizer program.\nThis program was created by fsb3rke.")

for i in range(2):
    print(f"This program will close after {2-i} second(s)", end="\r")
    time.sleep(1)
    
# Solve carriage return bug
print(end="\r")
