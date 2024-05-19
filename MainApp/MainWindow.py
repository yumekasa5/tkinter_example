# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog

# from SerialComControl.SerialComControl import SerialComControl
from ControlGUI.SettingDialog import SettingDialog
from ControlGUI.FigureCanvas import FigureCanvasFrame

class MainWindow(tk.Frame):
    def __init__(self, master=None, mode="user"):
        super().__init__(master)
        self.master = master
        self.mode = mode
        # self.serial_com = SerialComControl(port="COM3", baudrate=9600, timeout=0.5)
        self.pack()

        # Opearation mode
        self.mode = mode
        print("Operation mode: " + mode)

        self.width = 1920
        self.height = 1080
        master.geometry(str(self.width) + "x" + str(self.height))
        self.master.title("Tkinter GUI")
        self.svPath = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):

        # File Select Button
        self.fileSelectButton = tk.Button(text="Select", width=15, height=2, font=("Meyrio", 12))
        self.fileSelectButton.place(x=0, y=300)
        self.fileSelectButton.bind("<ButtonPress>", self.openFileDialog)
        
        # COM Port Select Spinbox
        self.validate_com_port = self.master.register(self.validate_com_port)
        self.comPortLabel = tk.Label(text="COM Port :", width=10, height=2, font=("Meyrio", 12))
        self.comPortLabel.place(x=20, y=10)
        self.comPortSpinbox = tk.Spinbox(from_=1, to=10, validate="key", width=3, validatecommand=(self.validate_com_port, '%P'), font=("Meyrio", 12))
        self.comPortSpinbox.setvar(name="COM Port", value="3")
        self.comPortSpinbox.place(x=125, y=20)
        

        # Table
        # self.treeView = ttk.Treeview(self.master, columns=["ID", "Name", "Score"])
        # # Column settings
        # self.treeView.column('#0', width=0, stretch='no')
        # self.treeView.column('ID', anchor='center', width=80)
        # self.treeView.column('Name', anchor='w', width=100)
        # self.treeView.column('Score', anchor='center', width=80)
        # # Column headers
        # self.treeView.heading('#0', text="check")
        # self.treeView.heading('ID', text='ID', anchor='center')
        # self.treeView.heading('Name', text='Name', anchor='w')
        # self.treeView.heading('Score', text='Score', anchor='center')
        # # Record insertion
        # self.treeView.insert(parent='', index='end', iid=0, values=("☐", 1, 'KAWASAKI', 80))
        # self.treeView.insert(parent='', index='end', iid=1, values=("☐", 2, 'SHIMIZU', 90))
        # self.treeView.insert(parent='', index='end', iid=2, values=("☐", 3, 'TANAKA', 45))
        # self.treeView.insert(parent='', index='end', iid=3, values=("☐", 4, 'OKABE', 60))
        # # Widget placement
        # self.treeView.place(x=5, y=5)
        # self.treeView.bind("<<TreeviewSelect>>", self.toggle_checkbox)

        # ListBox
        color_list = ["red", "blue", "green"]
        color_v = tkinter.StringVar(self.master, value=color_list)
        self.sampleListBox = tk.Listbox(self.master, width=10, height=5, listvariable=color_v, font=("Meyrio", 12))
        self.sampleListBox.place(x=200, y=300)

        # Check ListBox status button
        self.checkBtn = tk.Button(text="Check", width=15, height=2, font=("Meyrio", 12))
        self.updateCanvasButton = tk.Button(text="Update", width=15, height=2, font=("Meyrio", 12), command=self.update_canvas)
        self.updateCanvasButton.place(x=1000, y=500)
        
        # Open Setting Dialog Button
        self.settingButton = tk.Button(text="Setting", width=15, height=2, font=("Meyrio", 12))
        self.settingButton.place(x=0, y=400)
        self.settingButton.bind("<ButtonPress>", self.openSettingDialog)
        self.settingButton.place(x=0, y=400)
        
        # FigureCanvas
        self.canvas_frame = tk.Frame(self.master)
        self.canvas_frame.place(x=1000, y=10)
        self.canvas = FigureCanvasFrame(master=self.canvas_frame)
        self.update_canvas()

    def validate_com_port(self, value):
        if value == "":
            return True
        try:
            int(value)
        except ValueError:
            return False
        return True
    
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
        print(f"Selected file path: {path}")
        return "break"

    def openSettingDialog(self, event):
        """Open Setting Dialog"""
        print("Setting Dialog open.")
        setting_dialog = SettingDialog(self)
        # self.master.wait_window(setting_dialog)
        return "break"

    check_str = {"uncheck": "☐", "checked": "☑"}  # ☐☑☒ Checkbox characters
    def toggle_checkbox(self, event):
        row_id = self.treeView.focus()
        row_vals = self.treeView.item(row_id, "values")
        if row_vals[0] == self.check_str["uncheck"]:
            self.treeView.item(row_id, values=(self.check_str["checked"], row_vals[1], row_vals[2], row_vals[3]))
        else:
            self.treeView.item(row_id, values=(self.check_str["uncheck"], row_vals[1], row_vals[2], row_vals[3]))

    # Function to add IDs of rows with ☑ in the first column of Treeview to the ListBox
    def add_checked_ids_to_listbox(self):
        checked_ids = []
        for item in self.treeView.get_children():
            values = self.treeView.item(item, "values")
            if values[0] == self.check_str["checked"]:
                checked_ids.append(values[1])
        self.sampleListBox.delete(0, tk.END)
        for id in checked_ids:
            self.sampleListBox.insert(tk.END, id)
            
    def update_canvas(self):
        self.canvas.update()
