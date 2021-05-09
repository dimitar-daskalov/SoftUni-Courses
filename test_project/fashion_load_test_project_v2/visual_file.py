from tkinter import *
import tkinter.messagebox
import os
from hardcoded_logic_file import open_folder, raw_data_directory, original_working_directory, \
    move_files, is_empty
import sys


# message pop when no files can be found in the opened folder
def show_message():
    tkinter.messagebox.showinfo("Error!", "No files available!")


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# absolute path to the icon
path_icon = resource_path("images/launcher_icon.ico")

tk = Tk()
tk.title("Fashion Load")
tk.iconbitmap(path_icon)
tk.resizable(width=False, height=False)
tk.geometry('320x260')

# absolute path to the raw data folder button image
path_open_raw_data_folder_button_image = resource_path("images/open_raw_data_folder_button.png")
# open raw data folder button image
open_raw_data_folder_button_img = PhotoImage(file=path_open_raw_data_folder_button_image)

# absolute path to the fashion folder button image
path_open_fashion_folder_button_image = resource_path("images/open_fashion_folder_button.png")
# open fashion folder button image
open_fashion_folder_button_img = PhotoImage(file=path_open_fashion_folder_button_image)

# absolute path to the load data files button image
path_load_data_files_button_image = resource_path("images/upload_button.png")
# load data files button image
load_data_files_button_img = PhotoImage(file=path_load_data_files_button_image)

# absolute path to the exit button image
path_exit_button_image = resource_path("images/exit_button.png")
# exit button image
exit_button_img = PhotoImage(file=path_exit_button_image)

# open raw data folder button text, placement and functionality
open_raw_data_folder_button_text = Label(text="Open raw data", font="Minion 11 bold")
open_raw_data_folder_button_text.place(x=20, y=30)
open_raw_data_folder_button = Button(tk, image=open_raw_data_folder_button_img, borderwidth=0)
open_raw_data_folder_button.place(x=40, y=57)
open_raw_data_folder_button.config(command=lambda: open_folder(raw_data_directory))

# open fashion folder button text, placement and functionality
open_fashion_folder_button_text = Label(text="Open fashion", font="Minion 11 bold")
open_fashion_folder_button_text.place(x=200, y=30)
open_fashion_folder_button = Button(tk, image=open_fashion_folder_button_img, borderwidth=0)
open_fashion_folder_button.place(x=220, y=57)
open_fashion_folder_button.config(command=lambda: open_folder(original_working_directory))

# load files button text, placement and functionality
load_data_files_button_button_text = Label(text="Load data files", font="Minion 11 bold")
load_data_files_button_button_text.place(x=20, y=140)
load_data_files_button_button = Button(tk, image=load_data_files_button_img, borderwidth=0)
load_data_files_button_button.place(x=40, y=167)
load_data_files_button_button.config(
    command=lambda: move_files() if not is_empty() else show_message())

# exit button text, placement and functionality
exit_button_text = Label(text="Exit program", font="Minion 11 bold")
exit_button_text.place(x=200, y=140)
exit_button = Button(tk, image=exit_button_img, borderwidth=0)
exit_button.place(x=220, y=167)
exit_button.config(command=lambda: tk.destroy())

tk.mainloop()
