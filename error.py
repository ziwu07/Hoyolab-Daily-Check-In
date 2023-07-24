from tkinter import messagebox
import inspect
import os

def show_error_message(message:str = 'unknown error'):
    caller_frame = inspect.currentframe().f_back
    caller_filepath = caller_frame.f_code.co_filename
    caller_filename = os.path.basename(caller_filepath)
    messagebox.showerror(title=caller_filename, message=message)

def show_info(message:str = 'info'):
    messagebox.showinfo('Info', message=message)
