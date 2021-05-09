import os
import shutil
import webbrowser

# open folder directory paths
original_working_directory = r"\\Dcew1164prodinf\TRAITEMENTS\SEPARATION_RUN\GJ\Fashion"
raw_data_directory = r"\\Dcew1164prodinf\RAWDATA"


# open folder function - opens a folder from the file manager
def open_folder(received_directory):
    webbrowser.open(received_directory)


# check if the open folder is empty and returns boolean depending on the result
def is_empty():
    source_directory = original_working_directory
    file_names = os.listdir(source_directory)
    return not file_names


# move the files from the opened directory to the loading script folder directory
def move_files():
    source_directory = original_working_directory
    target_directory = r"\\Dcew1164prodinf\TRAITEMENTS\SEPARATION_RUN"
    file_names = os.listdir(source_directory)
    for file_name in file_names:
        shutil.move(os.path.join(source_directory, file_name), target_directory)
