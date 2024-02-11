# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5
import sys
import tkinter

from MainApp import MainWindow

def some_function():
    print("Function called.")

if __name__ == '__main__':
    args = sys.argv
    if len(args) != 0:
        for arg in args:
            print(arg)
            print(type(arg))
            
    root = tkinter.Tk()
    app = MainWindow.MainWindow(master=root)
    app.mainloop()
    