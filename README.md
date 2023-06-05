# Categorizer
A tool for categorize files into spesific folders

## Usage
Start with python
```sh
python categorizer/main.py
```

 ## Installation
Github to clone the project.
```sh
git clone https://github.com/fsb3rke/categorizer.git
```
Python to start the project
```sh
python categorizer/main.py
```

## Data
| PDFs | IMAGES | DOCUMENTS | DATA | ARCHIVES | EXECUTABLES | MUSICS | VIDEOS |
| ---- | ------ | --------- | ---- | -------- | ----------- | ------ | ------ |
| pdf | png | doc | csv | zip | exe | mp3 | mp4 |
| | jpg | docx | xlsx | rar | | wav | avi |
| | jpeg | txt | | | | | flv |
| | gif | | | | | | wmv

## Methods
[win.py]
```python
def list_files(directory) -> list
# It's based on listdir() function but this method lists only files to append files list.
```
```python
def init_folders() -> list
# It creates data folders like PDFs or IMAGES. And returns base file names in a list.
```
```python
def set_categorize_files(file_list: list, directory) -> dict
# It sets categorize to files in a single header.

# Output like
{PDFs: ["~/Desktop/coop_note_book.pdf"]}
```
```python
def move_file_to_directories(file_path: str, move_path: str)
# file_path is where is the file real path. move_path is where it'll move.
# file_path reading in binary mode to in a variable and another file writing with this data.
# file_path removing with os.remove() method.
```

## Screenshots
<details>
           <summary>Show Categorizer</summary>
           <p align="center">
              <img src="https://github.com/fsb3rke/categorizer/blob/master/gitphoto/image0.png">
           </p>
</details>
<details>
           <summary>Show Categorizer's Power</summary>
           <p align="center">
              <img src="https://github.com/fsb3rke/categorizer/blob/master/gitphoto/image1.png">
           </p>
</details>

## RoadMap
- Add more extension type for data

## License
Copyright (c) 2023 Berke Avcı (fsb3rke) \
\
This software is released under the [MIT](https://choosealicense.com/licenses/mit/) License.
