import tkinter as tk
from tkinter import ttk

class SettingDialog(tk.Toplevel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.title("Setting Dialog")
        self.geometry("300x240")

        # Create and place the widgets
        self.com_label = ttk.Label(self, text="COM:", anchor="w")
        self.com_label.pack()

        self.com_entry = ttk.Entry(self)
        self.com_entry.pack()

        self.baud_label = ttk.Label(self, text="Baud Rate:", anchor="w")
        self.baud_label.pack()

        self.baud_entry = ttk.Entry(self)
        self.baud_entry.pack()

        self.start_label = ttk.Label(self, text="Start Bit:", anchor="w")
        self.start_label.pack()

        self.start_entry = ttk.Entry(self)
        self.start_entry.pack()

        self.stop_label = ttk.Label(self, text="Stop Bit:", anchor="w")
        self.stop_label.pack()

        self.stop_entry = ttk.Entry(self)
        self.stop_entry.pack()

        self.data_label = ttk.Label(self, text="Data Byte:", anchor="w")
        self.data_label.pack()

        self.data_entry = ttk.Entry(self)
        self.data_entry.pack()

        self.save_button = ttk.Button(self, text="Save", command=self.save_settings)
        self.save_button.pack()

    def save_settings(self):
        com = self.com_entry.get()
        baud = self.baud_entry.get()
        start_bit = self.start_entry.get()
        stop_bit = self.stop_entry.get()
        data_byte = self.data_entry.get()

        # TODO: Save the settings to a file or perform any other necessary actions

        self.destroy()
