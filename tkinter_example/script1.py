import logging
import tkinter as tk

#ロガーの生成
logger = logging.getLogger('mylog')

#出力レベルの設定
logger.setLevel(logging.DEBUG)

#ハンドラの設定
handler = logging.FileHandler('./logs/logfile.log')

#フォーマッタの生成
fmt = logging.Formatter('%(asctime)s%(message)s')
handler.setFormatter(fmt)

#ハンドラをloggerに追加
logger.addHandler(handler)

debug_msg = 'debug message'
error_msg = 'error_message'

def pushed(b):
    b['text'] = 'clicked'
    print('clicked')

def main():
    root = tk.Tk()
    root.title('Tkinter example')
    #メインウィンドウを640x480にする
    root.geometry('640x480')
    label = tk.Label(root, text='Hello,World')
    label.grid()
    button = tk.Button(root, text='Button', command= lambda : pushed(button))
    button.grid()
    root.mainloop()

    # logger.debug('[START] My System Start')
    print('[SUCCESS] py -m  myproject')