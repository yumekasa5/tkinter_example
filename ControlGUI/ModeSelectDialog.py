# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5
import tkinter as tk

class ModeSelectDialog(tk.Frame):
    """Mode Select Dialog"""
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.grid(sticky='nsew')
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.mode_String = tk.StringVar()
        self.create_widgets()
        self.master.geometry("300x80")  # Set the size of the dialog window
        self.master.title("Select Mode")  # Set the title of the dialog window

    def create_widgets(self):
        self.label = tk.Label(text="Select operation mode")
        self.label.grid(row=0, column=0, columnspan=3)
        self.button_admin = tk.Button(text="Admin", command=lambda: self.set_admin("admin"), width=10)
        self.button_admin.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)  # Center align the button
        self.button_develop = tk.Button(text="Develop", command=lambda: self.set_develop("develop"), width=10)
        self.button_develop.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)  # Center align the button
        self.button_user = tk.Button(text="User", command=lambda: self.set_user("user"), width=10)
        self.button_user.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)  # Center align the button

    def set_admin(self, mode):
        self.mode_String.set(mode)
        self.master.destroy()

    def set_develop(self, mode):
        self.mode_String.set(mode)
        self.master.destroy()

    def set_user(self, mode):
        self.mode_String.set(mode)
        self.master.destroy()
