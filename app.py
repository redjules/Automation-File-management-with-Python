import os
import shutil
import argparse

# define file categories
FILE_CATEGORIES = {
    'Images' : ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents' : ['.pdf', '.docx', '.text', '.xlsx'],
    'Videos' : ['.mp4', '.mov', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Scripts' : ['.py', '.js', '.html', '.css'] 

}

def organize_files(directory):
    # create folders based on categories
    for category in FILE_CATEGORIES:
        folder_path = os.path.join(directory, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    # move files into the appropriate folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # skip directories
        if os.path.isdir(file_path):
            continue
        file_extension = os.path.splitext(filename)[1].lower()

        # check which category the file belongs to
        move = False
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                shutil.move(file_path, os.path.join(directory, category, filename))
                moved = True
                break
        # if the file does not belong to any category, move it to Other folder
        if not moved:
            others_folder = os.path.join(directory, 'Others')
            if not os.path.exists(others_folder):
               os.makedirs(others_folder)
            shutil.move(file_path, os.path.join(others_folder, filename))
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Organize files in a directory based on file types.')
    parser.add_argument('directory', type=str, help='The directory to organize')

    args = parser.parse_args()
    organize_files(args.directory)
    print("Files have been organized successfully !")


