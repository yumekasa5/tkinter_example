# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5
import sys
import tkinter

from MainApp import MainWindow
from ControlGUI.ModeSelectDialog import ModeSelectDialog

if __name__ == "__main__":
    is_gui_mode = True
    mode = "user"
    args = sys.argv
    if len(args) != 1:
        if args[1] == "-c" or args[1] == "--console":
            is_gui_mode = False
            path = args[2]
            print(path)
        elif args[1] == "-d" or args[1] == "--develop":
            mode = "develop"
        elif args[1] == "-a" or args[1] == "--admin":
            mode = "admin"
        elif args[1] == "-u" or args[1] == "--user":
            pass
        
    if is_gui_mode:        
        root = tkinter.Tk()
        # root.withdraw() # hide root window
        modeSelectDiaglog = ModeSelectDialog(master=root)
        # mode = diaglog.mode_String.get()
        modeSelectDiaglog.mainloop()

        # root.deiconify() # show root window
        app = MainWindow.MainWindow(master=root, mode=mode)
        app.mainloop()
    