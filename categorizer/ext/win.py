import os
import data

def list_files(directory) -> list:
    files = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            files.append(item_path)
    
    return files

def init_folders():
    DATAs = [data.PDFs, data.IMAGES, data.DOCUMENTS, data.DATA, data.ARCHIVES, data.EXECUTABLES, data.MUSICS, data.VIDEOS]
    for i in DATAs:
        os.mkdir(i)