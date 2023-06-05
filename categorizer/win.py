import os
from data import *

def list_files(directory) -> list:
    files = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            files.append(item_path)
    
    return files

def init_folders() -> list:
    datas = [PDFs, IMAGES, DOCUMENTS, DATA, ARCHIVES, EXECUTABLES, MUSICS, VIDEOS]
    try:
        for i in datas:
            os.mkdir(i)
        
    except FileExistsError:
        # # print("Folder already created. Please delete all folders and move your files into your current root folder. This data folders returns empty list to program.")
        pass

    return datas

def set_categorize_files(file_list: list, directory) -> dict:
    categorized_files: dict = {PDFs: [], IMAGES: [], DOCUMENTS: [], DATA: [], ARCHIVES: [], EXECUTABLES: [], MUSICS: [], VIDEOS: []}
    for i in file_list:
        # file_name_N_extension = i.split(".")[-1] # aa.txt.exe -> [aa, txt, exe] -> [exe, txt, aa] > exe
        file_extension = i.split(".")[-1]
        data_extension = EXTENSIONS[file_extension]
        categorized_files[data_extension].append(i)
        # print(f"IN: SET_CATEGORIZE_FILES ===> FILE_EXTENSION(${file_extension}) | DATA_EXTENSION(${data_extension}) | CATEGORIZED_FILE(${categorized_files})")

    return categorized_files

def move_file_to_directories(file_path: str, move_path: str):
    # Read the file in binary mode and set the new file which as created on new path.
    first_file_data = open(file_path, "rb").read()
    moved_file_data = open(move_path, "wb").write(first_file_data)
    os.remove(file_path)
