from tkinter import *
import tkinter.messagebox

from hardcoded_logic_file import open_folder, move_files, is_empty


def show_message():
    tkinter.messagebox.showinfo("Error!", "No files available!")


tk = Tk()
tk.title("Fashion Load - Test project v2")
tk.resizable(width=False, height=False)
tk.geometry('320x180')

open_folder_button = Button(tk, text="Open folder", bg="blue", fg="white", height=2, width=10)
open_folder_button.place(x=30, y=70)
open_folder_button.config(command=lambda: open_folder())

load_files_button = Button(tk, text="Load files", bg="green", fg="white", height=2, width=10)
load_files_button.place(x=200, y=70)
load_files_button.config(
    command=lambda: move_files() if not is_empty() else show_message())

tk.mainloop()
