import os
import shutil


def move_files():
    """Moves all files with the same prefix name to a different folder,
    allows user to specify type of file to move"""
    # asks user for input with the folder path, destination folder path and
    # the file name to look for
    src_dir = input("Enter the source folder path: ")
    while not os.path.exists(src_dir):
        src_dir = input("Please enter a valid source folder path: ")
    dst_dir = input("Enter the destination folder path: ")
    while not os.path.exists(dst_dir):
        dst_dir = input("Please enter a valid destination folder path: ")
    target_filename = input("Enter the file name to look for: ")
    # allow user to specify a file type to move
    file_type = input("Enter the file type to move, otherwise just enter 'n': ")
    # iterates through the source folder and moves all files
    # with the same prefix name to the destination folder
    for filename in os.listdir(src_dir):
        if filename.startswith(target_filename) and\
             os.path.isfile(f"{src_dir}/{filename}"):
            if filename.endswith(file_type):
                shutil.move(f"{src_dir}/{filename}", f"{dst_dir}/{filename}")


# if __name__ == '__main__':
#     print(main())
