import os
import shutil
import webbrowser
import re

initial_directory = r"\\DCEW1164FSCEB01\Data\GFK_CEB\IN\BOOK"
monthly_directory = r"\\Dcew1164prodinf\TRAITEMENTS\EXTRACTIONS\CEB\LIVRE\Mensuels"
needed_file_names = ["28", "47", "68", "75"]
needed_file_names_and_retailers_dict = {"28": "CASTORAMA", "47": "BRICORAMA", "68": "COOPAGRI", "75": "EURALIS"}


# check if a folder name is empty
def is_name_empty(name_received):
    return not name_received


# check if a folder with the same name already exists in the suggested directory
def is_the_same(name_received):
    file_names = os.listdir(monthly_directory)
    return name_received in file_names


# create a folder with a name given from the input in the suggested directory
def create_folder(name_received):
    os.chdir(monthly_directory)
    new_folder = name_received
    os.makedirs(new_folder)


# open the created folder
def open_current_folder(folder_name):
    current_directory = os.path.join(monthly_directory, folder_name)
    webbrowser.open(current_directory)


# move the detected files from the suggested directory to the current directory
def move_files(current_directory, possible_directory):
    file_names = os.listdir(possible_directory)

    for file_name in file_names:
        if file_name.split("_")[0] in needed_file_names:
            shutil.move(os.path.join(possible_directory, file_name), current_directory)


# locate and move the needed files to the created folder
def locate_and_move_the_needed_files(folder_name):
    current_directory = os.path.join(monthly_directory, folder_name)

    first_possible_directory = initial_directory
    second_possible_directory = monthly_directory
    third_possible_directory = r"\\Dcew1164prodinf\TRAITEMENTS\EXTRACTIONS\CEB\LIVRE"

    move_files(current_directory, first_possible_directory)
    move_files(current_directory, second_possible_directory)
    move_files(current_directory, third_possible_directory)

    file_names = os.listdir(current_directory)

    if len(file_names) == 0:
        return "Error!", f"No files were found!"
    elif len(file_names) == 4:
        return "Success!", "Successfully transferred all files!"
    elif len(file_names) < 4:
        existing_names_set = set([file_name.split("_")[0] for file_name in file_names if
                                  file_name.split("_")[0] in needed_file_names_and_retailers_dict])

        missing_names_set = set(needed_file_names).difference(existing_names_set)
        missing_names = [needed_file_names_and_retailers_dict[key] for key in needed_file_names_and_retailers_dict if
                         key in missing_names_set]
        return "Error!", f"Missing files for {', '.join(missing_names)}!"


# rename the files in the created folder using regular expressions
def rename_files(folder_name, needed_name):
    current_directory = os.path.join(monthly_directory, folder_name)
    file_names = os.listdir(current_directory)
    pattern = r'(\;[0-9]{4}\;[M]\;)|(\;[0-9]{4}\;[W]\;)'

    if not needed_name:
        return "Error!", "The period cannot be empty!"

    if not needed_name.isdigit():
        return "Error!", "The period should contain only numbers!"

    for file_name in file_names:
        with open(f"{os.path.join(current_directory, file_name)}", "r") as file:
            data_provided = file.read()

        needed_str = re.findall(pattern, data_provided)

        if needed_str:
            if not needed_str[0][0]:
                changed_info = data_provided.replace(needed_str[0][1], f";{needed_name};W;")
            else:
                changed_info = data_provided.replace(needed_str[0][0], f";{needed_name};W;")

            with open(f"{os.path.join(current_directory, file_name)}", "w") as f:
                f.write(changed_info)
            try:
                os.rename(os.path.join(current_directory, file_name),
                          os.path.join(current_directory, file_name.replace(file_name.split("_")[3], needed_name)))
            except IndexError:
                return "Error!", "The file name is incorrect!"
        else:
            return "Error!", "The file structure is incorrect!"

    return f"Success!", "Files renamed successfully!"


# copy and move the renamed files from the created folder to the initial directory using a temp folder,
# so all the data can be contained
def load_files(folder_name):
    current_directory = os.path.join(monthly_directory, folder_name)
    file_names = os.listdir(current_directory)
    os.chdir(current_directory)
    os.makedirs("Temp Folder")
    moving_directory = os.path.join(current_directory, "Temp Folder")
    if not file_names:
        return "Error!", "No files were found!"

    for file_name in file_names:
        shutil.copy(os.path.join(current_directory, file_name), moving_directory)

    moving_directory_file_names = os.listdir(moving_directory)

    for moving_directory_file_name in moving_directory_file_names:
        shutil.move(os.path.join(moving_directory, moving_directory_file_name), initial_directory)

    os.rmdir(moving_directory)

    return "Success!", "Files are loading!"
