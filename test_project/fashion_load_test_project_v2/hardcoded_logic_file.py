import os
import shutil
import webbrowser


def open_folder():
    webbrowser.open(("\\Dcew1164prodinf\TRAITEMENTS\SEPARATION_RUN\GJ\Fashion"))


def is_empty():
    source_directory = "\\Dcew1164prodinf\TRAITEMENTS\SEPARATION_RUN\GJ\Fashion"
    file_names = os.listdir(source_directory)
    if not file_names:
        return True
    return False


def move_files():
    source_directory = "\\Dcew1164prodinf\TRAITEMENTS\SEPARATION_RUN\GJ\Fashion"
    target_directory = "\\Dcew1164prodinf\TRAITEMENTS\SEPARATION_RUN"
    file_names = os.listdir(source_directory)
    for file_name in file_names:
        shutil.move(os.path.join(source_directory, file_name), target_directory)
