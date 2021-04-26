from tkinter import *
import tkinter.messagebox
import os
from hardcoded_logic_file import create_folder, is_the_same, is_name_empty, open_current_folder, \
    locate_and_move_the_needed_files, rename_files, load_files
import sys

# message pop when no files can be found in the opened folder
def show_message_no_files():
    tkinter.messagebox.showinfo("Error!", "No files available!")


# message pop when folder with than name already exists
def show_message_same_name():
    tkinter.messagebox.showinfo("Error!", "This folder already exists!")


# message pop when no folder name is added
def show_message_no_name_received():
    tkinter.messagebox.showinfo("Error!", "The name of the folder cannot be empty!")


# message pop when the folder is created successfully
def show_message_successfully_created(folder_name):
    tkinter.messagebox.showinfo("Success!", f"The folder {folder_name} was created!")


# message pop when locate and move func is used
def show_message_locate_and_move(folder_name):
    result = locate_and_move_the_needed_files(folder_name)
    tkinter.messagebox.showinfo(result[0], result[1])


# message pop when rename files func is used
def show_message_rename_files(folder_name, needed_name):
    result = rename_files(folder_name, needed_name)
    tkinter.messagebox.showinfo(result[0], result[1])

# message pop when load files func is used
def show_message_load_files(folder_name):
    result = load_files(folder_name)
    tkinter.messagebox.showinfo(result[0], result[1])


# clears the placeholder string
def clear_entry(event, entry):
    entry.delete(0, END)


# check if folder name is valid
def check_folder_name(name_received):
    if is_the_same(name_received):
        show_message_same_name()
    elif is_name_empty(name_received):
        show_message_no_name_received()
    else:
        create_folder(name_received)
        show_message_successfully_created(name_received)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# absolute path to the icon
path_icon = resource_path("images/book_icon.ico")

tk = Tk()
tk.title("Book - Monthly Entertainment")
tk.iconbitmap(path_icon)
tk.resizable(width=False, height=False)
tk.geometry('400x300')

# absolute path to the create folder image
path_create_folder_button_image = resource_path("images/create_folder_button.png")
# create folder button image
create_folder_button_img = PhotoImage(file=path_create_folder_button_image)

# create folder button text, placement and functionality
create_folder_button_text = Label(text="1. Folder name", font="Tahoma 11")
create_folder_button_text.place(x=30, y=10)
# get the folder name from the input
input_folder_name = Entry(tk, width=22, borderwidth=2)
input_folder_name.place(x=33, y=35)
input_folder_name.insert(0, "Enter folder name: ")
# clears the placeholder string on click
input_folder_name.bind("<Button-1>", lambda event: clear_entry(event, input_folder_name))
create_folder_button = Button(tk, image=create_folder_button_img, borderwidth=0)
create_folder_button.place(x=30, y=60)
# check if the folder name is valid and creates a folder
create_folder_button.config(command=lambda: check_folder_name(input_folder_name.get()))

# absolute path to the open folder image
path_open_folder_button_image = resource_path("images/open_folder_button.png")
# open folder button image
open_folder_button_img = PhotoImage(file=path_open_folder_button_image)

# open folder button text, placement and functionality
open_folder_button_text = Label(text="2. Open folder", font="Tahoma 11")
open_folder_button_text.place(x=230, y=10)
open_folder_button = Button(tk, image=open_folder_button_img, borderwidth=0)
open_folder_button.place(x=230, y=60)
# open the created folder
open_folder_button.config(command=lambda: open_current_folder(input_folder_name.get()))

# absolute path to the locate and move image
path_locate_and_move_button_image = resource_path("images/locate_and_move_button.png")
# locate and move button image
locate_and_move_button_img = PhotoImage(file=path_locate_and_move_button_image)

# locate and move files button text, placement and functionality
locate_and_move_button_text = Label(text="3. Locate and move", font="Tahoma 11")
locate_and_move_button_text.place(x=30, y=100)
locate_and_move_button = Button(tk, image=locate_and_move_button_img, borderwidth=0)
locate_and_move_button.place(x=30, y=150)
# locate and move the needed files to the folder
locate_and_move_button.config(command=lambda: show_message_locate_and_move(input_folder_name.get()))

# absolute path to the rename files image
path_rename_files_button_image = resource_path("images/rename_files_button.png")
# rename files button image
rename_files_button_img = PhotoImage(file=path_rename_files_button_image)

# rename files button text, placement and functionality
rename_files_button_text = Label(text="4. Rename files", font="Tahoma 11")
rename_files_button_text.place(x=230, y=100)
rename_button_input_folder_name = Entry(tk, width=22, borderwidth=2)
rename_button_input_folder_name.place(x=233, y=125)
rename_button_input_folder_name.insert(0, "Enter period: ")
# clears the placeholder string on click
rename_button_input_folder_name.bind("<Button-1>", lambda event: clear_entry(event, rename_button_input_folder_name))
rename_files_button = Button(tk, image=rename_files_button_img, borderwidth=0)
rename_files_button.place(x=230, y=150)
# renames the needed files
rename_files_button.config(command=lambda: show_message_rename_files(
    input_folder_name.get(), rename_button_input_folder_name.get()))

# absolute path to the load button image
path_load_button_image = resource_path("images/load_files_button.png")
# load button image
load_button_img = PhotoImage(file=path_load_button_image)

# load button text, placement and functionality
load_button_text = Label(text="5. Load files", font="Tahoma 11")
load_button_text.place(x=30, y=190)
load_button = Button(tk, image=load_button_img, borderwidth=0)
load_button.place(x=30, y=240)
# copies the renamed files from the created folder to the initial directory
load_button.config(command=lambda: show_message_load_files(input_folder_name.get()))

# absolute path to the quit button image
path_quit_button_image = resource_path("images/exit_button.png")
# quit button image
quit_button_img = PhotoImage(file=path_quit_button_image)

# quit button text, placement and functionality
quit_button_text = Label(text="6. Exit program", font="Tahoma 11")
quit_button_text.place(x=230, y=190)
quit_button = Button(tk, image=quit_button_img, borderwidth=0, command=lambda: tk.destroy())
quit_button.place(x=230, y=240)


tk.mainloop()
