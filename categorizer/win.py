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
    for i in datas:
        os.mkdir(i)
    
    return datas

def set_categorize_files(file_list: list, directory) -> dict:
    categorized_files: dict = {PDFs: [], IMAGES: [], DOCUMENTS: [], DATA: [], ARCHIVES: [], EXECUTABLES: [], MUSICS: [], VIDEOS: []}
    for i in file_list:
        # file_name_N_extension = i.split(".")[-1] # aa.txt.exe -> [aa, txt, exe] -> [exe, txt, aa] > exe
        file = i.split(".")
        file_name = file[0]
        file_extension = file[-1] # i think this is more readable
        data_extension = EXTENSIONS[file_extension]
        categorized_files[data_extension].append(os.path.join(f"{file_name}.{file_extension}", directory))

    return categorized_files

def move_file_to_directories():
    pass