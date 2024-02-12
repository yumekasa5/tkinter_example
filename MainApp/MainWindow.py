# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5
import tkinter as tk

class MainWindow(tk.Frame):
    def __init__(self, master=None, mode="user"):
        super().__init__(master)
        self.pack()
        
        # 起動モード
        self.mode = mode
        print("Opearation mode:" + mode)
        
        self.width = 1150
        self.height = 800
        master.geometry(str(self.width) + "x" + str(self.height))
        self.master = master
        self.master.geometry("640x480")
        self.master.title("Seirial Command Tool")
        self.create_widgets()
        
    def create_widgets(self):
        
        # Button
        self.press1Button = tk.Button(text="Press", width=18)
        self.press1Button.place(x=0, y= 300)
        self.press1Button.bind("<ButtonPress>", self.puressed)
    
    def callback(self):
        pass

    def puressed(self, event):
        print('clicked')