# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog

from ControlGUI import Figure

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
        self.svPath = tk.StringVar()
        self.create_widgets()
        self.figure_frame = Figure.createFigure(self.master)
        self.figure_frame.place(x=300, y=5)
        
    def create_widgets(self):
        
        # File Select Button
        self.fileSelectButton = tk.Button(text="Select", width=18)
        self.fileSelectButton.place(x=0, y= 300)
        self.fileSelectButton.bind("<ButtonPress>", self.openFileDialog)
        
        # Table
        self.tableData = ttk.Treeview(self.master, columns=["ID", "Name", "Score"])
       # 列の設定
        self.tableData.column('#0',width=0, stretch='no')
        self.tableData.column('ID', anchor='center', width=80)
        self.tableData.column('Name',anchor='w', width=100)
        self.tableData.column('Score', anchor='center', width=80)
        # 列の見出し設定
        self.tableData.heading('#0',text='')
        self.tableData.heading('ID', text='ID',anchor='center')
        self.tableData.heading('Name', text='Name', anchor='w')
        self.tableData.heading('Score',text='Score', anchor='center')
        # レコードの追加
        # self.tableData.insert(parent='', index='end', iid=0 ,values=(1, 'KAWASAKI',80))
        # self.tableData.insert(parent='', index='end', iid=1 ,values=(2,'SHIMIZU', 90))
        # self.tableData.insert(parent='', index='end', iid=2, values=(3,'TANAKA', 45))
        # self.tableData.insert(parent='', index='end', iid=3, values=(4,'OKABE', 60))
        # self.tableData.insert(parent='', index='end', iid=4, values=(5,'MIYAZAKI', 99))
        # ウィジェットの配置
        self.tableData.place(x=5, y=5)
        
        # ListBox
        color_list = ["red", "blue", "green"]
        color_v = tkinter.StringVar(self.master, value=color_list)
        self.sampleListBox = tk.Listbox(self.master, height=5, listvariable=color_v)
        self.sampleListBox.place(x=200, y=300)

        # Check Listbox status button
        self.checkBtn = tk.Button(text="Check", width=18)
        self.checkBtn.place(x=500, y= 300)
        self.checkBtn.bind("<ButtonPress>", self.checkListBoxStatus)
        
        # Delete button from ListBox
        self.deleteBtn = tk.Button(text="Delete", width=18)
        self.deleteBtn.place(x=500, y= 400)
        self.deleteBtn.bind("<ButtonPress>", self.deleteDataFromListBox)
        
    def checkListBoxStatus(self, event):
        print(f"ListBox(ACTIVE):{self.sampleListBox.get(tk.ACTIVE)}")
        print(f"ListBox(CurSelect):{self.sampleListBox.curselection()}")

    def deleteDataFromListBox(self, event):
        index = self.sampleListBox.curselection()
        self.sampleListBox.delete(index)

    def openFileDialog(self, event):
        """Open File Dialog and return string of file path"""
        print("File Dialog open.")
        path = ""
        path = tkinter.filedialog.askopenfilename()
        print(f"Selected file path:{path}")
        return "break"
        