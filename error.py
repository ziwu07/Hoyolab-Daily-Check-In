from tkinter import messagebox
from datetime import datetime

LOG_FILE = "./logfile.log"


def show_error_message(message: str = "unknown error"):
    log(message=message, level="err")
    messagebox.showerror(title="daily check in script", message=message)


def show_info(message: str = "info"):
    log(message=message, level="info")
    messagebox.showinfo("Info", message=message)


def log(message: str, level: str = "debug"):
    with open(LOG_FILE, "a") as file:
        file.write(f"{datetime.now()} | {level}: {message}")
