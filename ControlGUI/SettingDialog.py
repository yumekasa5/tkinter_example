# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5
import tkinter as tk
from tkinter import ttk

class SettingDialog(tk.Toplevel):
    """Digaolog for setting the serial communication parameters"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.title("Setting Dialog")
        self.geometry("300x500")

        # COM Port
        self.com_port_String = tk.StringVar()
        self.com_port_String.set("COM3")
        self.com_label = tk.Label(self, text="COM:", anchor="w", width=10, font=("Meyrio", 12))
        self.com_label.place(x=10, y=10)
        self.com_entry = ttk.Entry(self, textvariable=self.com_port_String, width=10, font=("Meyrio", 12))
        self.com_entry.place(x=100, y=10)

        # Baud Rate
        self.baud_String = tk.StringVar()
        self.baud_String.set("9600")
        self.baud_label = tk.Label(self, text="Baud Rate:", anchor="w", width=10, font=("Meyrio", 12))
        self.baud_label.place(x=10, y=40)
        self.baud_entry = ttk.Entry(self, textvariable=self.baud_String, width=10, font=("Meyrio", 12))
        self.baud_entry.place(x=100, y=40)

        # Start Bit
        self.start_String = tk.StringVar()
        self.start_String.set("1")
        self.start_label = tk.Label(self, text="Start Bit:", anchor="w", width=10, font=("Meyrio", 12))
        self.start_label.place(x=10, y=70)
        self.start_entry = ttk.Entry(self, textvariable=self.start_String, width=10, font=("Meyrio", 12))
        self.start_entry.place(x=100, y=70)

        # Stop Bit
        self.stop_string = tk.StringVar()
        self.stop_string.set("1")
        self.stop_label = tk.Label(self, text="Stop Bit:", anchor="w", width=10, font=("Meyrio", 12))
        self.stop_label.place(x=10, y=100)
        self.stop_entry = ttk.Entry(self, textvariable=self.stop_string, width=10, font=("Meyrio", 12))
        self.stop_entry.place(x=100, y=100)

        # Data Byte
        self.data_String = tk.StringVar()
        self.data_String.set("8")
        self.data_label = tk.Label(self, text="Data Byte:", anchor="w", width=10, font=("Meyrio", 12))
        self.data_label.place(x=10, y=130)
        self.data_entry = ttk.Entry(self, textvariable=self.data_String, width=10, font=("Meyrio", 12))
        self.data_entry.place(x=100, y=130)

        # OK Button
        self.okButton = tk.Button(self, text="OK", width=10, height=2, font=("Meyrio", 12))
        self.okButton.bind("<ButtonPress>", self.save_settings)
        self.okButton.place(x=10, y=200)
        
        # Cancel Button
        self.cancelButton = tk.Button(self, text="Cancel", width=10, height=2, font=("Meyrio", 12))
        self.cancelButton.bind("<ButtonPress>", self.cancel_settings)
        self.cancelButton.place(x=100, y=200)
        
        # Apply Button
        self.applyButton = tk.Button(self, text="Apply", width=10, height=2, font=("Meyrio", 12))
        self.applyButton.bind("<ButtonPress>", self.apply_settings)
        self.applyButton.place(x=190, y=200)

    def save_settings(self, event):
        com = self.com_entry.get()
        baud = self.baud_entry.get()
        start_bit = self.start_entry.get()
        stop_bit = self.stop_entry.get()
        data_byte = self.data_entry.get()

        # TODO: Save the settings to a file or perform any other necessary actions

        self.destroy()
        
    def cancel_settings(self, event):
        self.destroy()
        
    def apply_settings(self, event):
        com = self.com_entry.get()
        baud = self.baud_entry.get()
        start_bit = self.start_entry.get()
        stop_bit = self.stop_entry.get()
        data_byte = self.data_entry.get()
