# File Organizer

This Python script organizes files in a specified directory into categorized folders based on their file types. The script will create folders such as `Images`, `Documents`, `Videos`, `Music`, `Scripts`, and `Others`, and move the files into the appropriate folder.

## Features

- Organizes files into predefined categories:
  - **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`
  - **Documents**: `.pdf`, `.docx`, `.text`, `.xlsx`
  - **Videos**: `.mp4`, `.mov`, `.avi`
  - **Music**: `.mp3`, `.wav`
  - **Scripts**: `.py`, `.js`, `.html`, `.css`
- Files that do not fit into any of these categories are moved to an `Others` folder.
- Creates folders dynamically if they do not exist.

## Requirements

- Python 3.x
- The following modules are used (which are part of Python's standard library):
  - `os`
  - `shutil`
  - `argparse`

## Usage

1. Clone or download this repository.
2. Run the script with the directory you want to organize as an argument.

python organize_files.py <directory_path>

Example:

python organize_files.py /path/to/your/directory

This will organize the files in the specified directory based on their file type.

## How It Works?

The script checks all the files in the directory.

Files are categorized based on their extension into folders such as Images, Documents, Videos, Music, and Scripts.

Files with extensions that do not match the predefined categories are moved to an Others folder.

Folders for each category are created if they do not exist already.
