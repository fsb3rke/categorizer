PDFs = 0
IMAGES = 1
DOCUMENTS = 2
DATA = 3
ARCHIVES = 4
EXECUTABLES = 5
MUSICS = 6
VIDEOS = 7

EXTENSIONS: dict = {
    "pdf": PDFs,
    "png": IMAGES,
    "jpg": IMAGES,
    "jpeg": IMAGES,
    "gif": IMAGES,
    "doc": DOCUMENTS,
    "docx": DOCUMENTS,
    "txt": DOCUMENTS,
    "csv": DATA,
    "xlsx": DATA,
    "zip": ARCHIVES,
    "rar": ARCHIVES,
    "exe": EXECUTABLES,
    "mp3": MUSICS,
    "wav": MUSICS,
    "mp4": VIDEOS,
    "avi": VIDEOS,
    "flv": VIDEOS,
    "wmv": VIDEOS
}