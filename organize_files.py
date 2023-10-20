from rename_files import rename_main
from move_files import move_files
from get_all_extensions import get_all_extensions
import os


def main():
    while 1:
        # asks user to see what they want to do
        user_choice = input("Enter 'r' to rename files, 'm' to move files, or 'g' to get all extensions in a certain directory: ")
        while user_choice != 'r' and user_choice != 'm' and user_choice != 'g':
            user_choice = input("Please only enter 'r', 'm', or 'g': ")
        if user_choice == 'r':
            rename_main()
        elif user_choice == 'm':
            move_files()
        elif user_choice == 'g':
            dir = input("Enter the directory to get all extensions: ")
            while not os.path.exists(dir):
                dir = input("Please enter a valid directory: ")
            print(get_all_extensions(dir))
        # asks user if they want to continue
        user_continue = input("Do you want to continue? (y/n): ")
        while user_continue != 'y' and user_continue != 'n':
            user_continue = input("Please only enter 'y' or 'n': ")
        if user_continue == 'n':
            break


if __name__ == '__main__':
    main()
