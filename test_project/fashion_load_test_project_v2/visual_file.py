from tkinter import *
import tkinter.messagebox
from hardcoded_logic_file import open_folder, move_files, is_empty
import os
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
path_icon = resource_path("images/start_icon_button.ico")

tk = Tk()
tk.title("Fashion Load")
tk.iconbitmap(path_icon)
tk.resizable(width=False, height=False)
tk.geometry('320x180')

# absolute path to the image
path_open_button_image = resource_path("images/open_button.png")
# open button image
open_button_img = PhotoImage(file=path_open_button_image)

# absolute path to the image
path_load_button_image = resource_path("images/upload_button.png")
# load files button image
load_button_img = PhotoImage(file=path_load_button_image)

# open button text, placement and functionality
open_folder_button_text = Label(text="Open folder", font="Minion 11 bold")
open_folder_button_text.place(x=30, y=35)
open_folder_button = Button(tk, image=open_button_img, borderwidth=0)
open_folder_button.place(x=30, y=60)
open_folder_button.config(command=lambda: open_folder())

# load files button text, placement and functionality
load_files_button_text = Label(text="Load files", font="Minion 11 bold")
load_files_button_text.place(x=230, y=35)
load_files_button = Button(tk, text="load files", image=load_button_img, borderwidth=0)
load_files_button.place(x=230, y=60)
load_files_button.config(
    command=lambda: move_files() if not is_empty() else show_message())

tk.mainloop()
