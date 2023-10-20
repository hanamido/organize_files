import os
from pathlib import Path


# class RenameFiles:
#     def __init__(self) -> None:
#         """
#         Constructor for RenameFiles class
#         """


# Function to rename multiple files
def rename_main() -> None:
    # path of the directory containing the raw files
    folder = input("Enter the folder path: ")
    files = {}
    for count, filename in enumerate(os.listdir(folder)):
        files[count] = filename
    print(files)
    while not check_dir_exists(folder):  # check if the directory exists
        folder = input("Please enter a valid folder path: ")
    rename_prefix = input("Enter the rename prefix: ")

    # TODO: Possibly refactor to divide each user choice into separate functions
    # ask user if they want to rename files with a specific extension
    with_ext = input("Do you want to rename files with a specific extension? (y/n): ")
    include_ext = ''
    if with_ext == 'y':
        include_ext = input("Enter the file extension to include: ")
        # if the file extension is not valid, ask user to enter a valid file extension
        include_ext = check_valid_ext(include_ext)
        rename_files_include(folder, rename_prefix, include_ext)
    # handle invalid user response
    while with_ext != 'y' and with_ext != 'n':
        with_ext = input("Please only enter 'y' or 'n': ")

    # ask user if they want to rename all files except those with a specific extension
    without_ext = input("Do you want to exclude a specific extension? (y/n): ")
    exclude_ext = ''
    exclude_ext_lst = []
    if without_ext == 'y':
        exclude_ext_total = input("Do you want to exclude multiple extensions? (y/n): ")
        if exclude_ext_total == 'y':
            exclude_ext_input = input("Enter the file extensions to exclude, separated by a space: ")
            exclude_ext_lst = exclude_ext_input.split(' ')
            # checks if the extension is valid
            for ext in exclude_ext_lst:
                exclude_ext = check_valid_ext(ext)
            rename_files_exclude_multiple(folder, rename_prefix, exclude_ext_lst)
        else:
            rename_files_exclude_single(folder, rename_prefix, exclude_ext)
    elif without_ext == 'n':
        # if the file extension is not valid, ask user to enter a valid file extension
        exclude_ext = check_valid_ext(exclude_ext)
        rename_files_exclude_single(folder, rename_prefix, exclude_ext)

    # handle invalid user response
    while without_ext != 'y' and without_ext != 'n':
        without_ext = input("Please only enter 'y' or 'n': ")

    # user wants to rename all files
    if with_ext == 'n' and without_ext == 'n':
        rename_all_files(folder, rename_prefix)


def check_dir_exists(folder: str) -> bool:
    """
    Check if the directory exists
    """
    return os.path.exists(f"{folder}")


def check_valid_ext(ext: str) -> str:
    """
    Check if the file extension entered is a valid file extension.
    Returns the valid string when user enters a valid extension
    """
    valid_ext = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']
    while ext not in valid_ext:
        ext = input("Please enter a valid file extension: ")
    return ext


def prevent_overwrite(dst: str,
                      folder: str,
                      rename_prefix: str,
                      file_count: int,
                      ext: str) -> str:
    """
    Prevents the program from overwriting files if the
    filename already exists
    """
    # if the file name already exists, get the next available count
    while os.path.exists(dst):
        dst = f"{rename_prefix}-{file_count+1}{ext}"
        file_count += 1
        dst = f"{folder}/{dst}"
    return dst


def rename_files_include(folder: str,
                         rename_prefix: str,
                         include_ext: str) -> None:
    """
    Rename only files with the specified extension
    """
    file_count = 0
    # iterate through each of the files in the folder
    for filename in os.listdir(folder):
        # get files with the specified extension
        if filename.endswith(include_ext):
            # get the extension of the file
            _, ext = os.path.splitext(filename)
            dst = f"{rename_prefix}-{file_count+1}{ext}"
            src = f"{folder}/{filename}"
            dst = f"{folder}/{dst}"
            # if file doesn't exist, just increment file_count
            if not os.path.exists(dst):
                file_count += 1
            # prevent overwriting files
            # if the file name already exists, get the next available count
            if os.path.exists(dst):
                dst = prevent_overwrite(dst, folder, rename_prefix, file_count, ext)
            # rename() function will rename all the files
            os.rename(src, dst)
    # TODO: fix bug to make sure that the rename count is correct


def rename_files_exclude_single(folder: str,
                         rename_prefix: str,
                         exclude_ext: str):
    file_count = 0
    # iterate through each of the files in the folder
    for filename in os.listdir(folder):
        if not filename.endswith(exclude_ext):
            # get the extension of the file
            _, ext = os.path.splitext(filename)
            dst = f"{rename_prefix}-{file_count+1}{ext}"
            src = f"{folder}/{filename}"
            dst = f"{folder}/{dst}"
            # prevent overwriting files
            if os.path.exists(dst):
                dst = prevent_overwrite(dst, folder, rename_prefix, file_count, ext)
            # rename() function will rename all the files
            file_count += 1
            os.rename(src, dst)


def rename_files_exclude_multiple(folder: str, rename_prefix: str, exclude_ext_lst: []):
    """Renames all files except those with the specified extensions in exclude_ext_lst"""
    file_count = 0
    # iterate through each of the files in the folder
    for filename in os.listdir(folder):
        _, ext = os.path.splitext(filename)
        ext_to_get = ext[1:]
        if ext_to_get not in exclude_ext_lst:
            # get the extension of the file
            dst = f"{rename_prefix}-{file_count+1}{ext}"
            src = f"{folder}/{filename}"
            dst = f"{folder}/{dst}"
            # prevent overwriting files
            if os.path.exists(dst):
                dst = prevent_overwrite(dst, folder, rename_prefix, file_count, ext)
            # rename() function will rename all the files
            file_count += 1
            os.rename(src, dst)


def rename_all_files(folder, rename_prefix):
    # iterate through each of the files in the folder
    for count, filename in enumerate(os.listdir(folder)):
        # check if the file is a file instead of a folder
        if os.path.isfile(f"{folder}/{filename}"):
            # get the extension of the file
            _, ext = os.path.splitext(filename)
            dst = f"{rename_prefix}-{count+1}{ext}"
            src = f"{folder}/{filename}"
            dst = f"{folder}/{dst}"
            # prevent overwriting files
            if os.path.exists(dst):
                dst = prevent_overwrite(dst, folder, rename_prefix, count, ext)
            # rename() function will rename all the files
            os.rename(src, dst)


# Driver Code
# if __name__ == '__main__':
#     # Calling main() function
#     main()
