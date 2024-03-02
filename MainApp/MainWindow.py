# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog

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
        self.tableData.pack(pady=10) 
    
    def callback(self):
        pass

    def openFileDialog(self, event):
        """Open File Dialog and return string of file path"""
        print("File Dialog open.")
        path = ""
        path = tkinter.filedialog.askopenfilename()
        print(f"Selected file path:{path}")
        