# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5
import tkinter as tk

class ModeSelectDialog(tk.Frame):
    """Mode Select Dialog"""
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.mode_String = tk.StringVar()
        self.create_widgets()
        self.master.geometry("400x300")  # Set the size of the dialog window
        self.master.title("Select Mode")  # Set the title of the dialog window

    def create_widgets(self):
        self.label = tk.Label(text="Select operation mode")
        self.label.pack()
        self.button_admin = tk.Button(text="Admin", command=lambda: self.set_admin("admin"))
        self.button_admin.pack()
        self.button_develop = tk.Button(text="Develop", command=lambda: self.set_develop("develop"))
        self.button_develop.pack()
        self.button_user = tk.Button(text="User", command=lambda: self.set_user("user"))
        self.button_user.pack()

    def set_admin(self, mode):
        self.mode_String.set(mode)
        self.master.destroy()

    def set_develop(self, mode):
        self.mode_String.set(mode)
        self.master.destroy()

    def set_user(self, mode):
        self.mode_String.set(mode)
        self.master.destroy()