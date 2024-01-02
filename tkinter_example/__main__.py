from tkinter import ttk

import tkinter as tk
from tkinter import messagebox

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.iconbitmap(default='./data/icon/yumekasa5.ico')
        self.root.title('yumekasa5')
        self.root.geometry('640x480')
        
        # Progress bar
        self.progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
        self.progress_bar.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Button
        self.load_button = tk.Button(root, text="Load Images", command=self.load_images)
        self.load_button.grid(row=2, column=0, pady=10)
        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.grid(row=2, column=1, pady=10)
        
        # Initialize
        self.loaded_images = 0
        self.total_images = 13
        self.load_images()

    def load_images(self):
        if self.loaded_images < self.total_images:
            self.loaded_images += 1
            self.progress_bar["value"] = (self.loaded_images / self.total_images) * 100
            self.root.after(1000, self.load_images)  # 1秒後に次の画像を読み込む
        else:
            messagebox.showinfo("Finished", "All images loaded!")
            
    def show_message(self):
        messagebox.showinfo("Message", "Hello, you clicked the button!")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
