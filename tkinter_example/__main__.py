import subprocess
import os
import sys
import tkinter as tk
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
    root = tk.Tk()
    root.title('Tkinter example')
    root.geometry('640x480')
    label = tk.Label(root, text='Hello,World')
    label.grid()
    button = tk.Button(root, text='Button', command= lambda : pushed(button))
    button.grid()
    root.mainloop()

    # logger.debug('[START] My System Start')
    # print('[SUCCESS] py -m  myproject')

if __name__ == "__main__":
    main()
