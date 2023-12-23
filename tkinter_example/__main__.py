import subprocess
import os
import sys
import tkinter as tk
from tkinter import messagebox
from pathlib import Path

def pushed(b):
    b['text'] = 'clicked'
    print('clicked')

def main():
    # current_directory = Path(__file__).resolve().parent
    # print(current_directory)
    # try:
    #     module_example_path = os.path.join(current_directory, 'script1.py')
    #     subprocess.run([sys.executable, module_example_path], check=True)
    #     # subprocess.run(["python", module_example_path], check=True)
    # except:
    #     print('EROOR')
    iconfile = './data/icon/yumekasa5.ico'
    root = tk.Tk()
    root.iconbitmap(default=iconfile)
    root.title('Tkinter example')
    root.geometry('640x480')
    label = tk.Label(root, text='Hello,World')
    label.grid()
    button = tk.Button(root, text='Button', command= lambda : pushed(button))
    button.grid()
    root.mainloop()
    messagebox.showerror('ERROR', 'Failed to collect images.')
    messagebox.showwarning('WARNING', 'Value is lower than the target.')
    sample = [i for i in range(100000)]
    sample2 = [i for i in range(10000)]
    print(str(sys.getsizeof(sample)) + 'Byte')
    print(str(sys.getsizeof(sample2)) + 'Byte')
    # logger.debug('[START] My System Start')
    # print('[SUCCESS] py -m  myproject')

if __name__ == "__main__":
    main()
