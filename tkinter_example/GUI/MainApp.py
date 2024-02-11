import tkinter as tk

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

    def configure_gui(self):
        self.master.title("Yumekasa5")
        self.master.geometry("500x500")
        self.master.resizable(False, False)

    def create_widgets(self):
        pass

if __name__ == '__main__':
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()