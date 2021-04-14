import os
import shutil

original_working_directory = r"X:\SEPARATION_RUN\GJ\Fashion"


def open_folder():
    open(original_working_directory)


def is_empty():
    source_directory = original_working_directory
    file_names = os.listdir(source_directory)
    if not file_names:
        return True
    return False


def move_files():
    source_directory = original_working_directory
    target_directory = r"X:\SEPARATION_RUN"
    file_names = os.listdir(source_directory)
    for file_name in file_names:
        shutil.move(os.path.join(source_directory, file_name), target_directory)
