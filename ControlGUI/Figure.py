# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
import numpy as np

x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x)

def createFigure(tk_root):
    # matplotlib配置用フレーム
    frame = tk.Frame(tk_root)
    # matplotlibの描画領域の作成
    fig = Figure(figsize=(2, 2))
    # 座標軸の作成
    ax = fig.add_subplot(1, 1, 1)
    line, = ax.plot(x, y)
    # matplotlibの描画領域とウィジェット(Frame)の関連付け
    fig_canvas = FigureCanvasTkAgg(fig, frame)
    # matplotlibのツールバーを作成
    toolbar = NavigationToolbar2Tk(fig_canvas, frame)
    # matplotlibのグラフをフレームに配置
    fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    # フレームをウィンドウに配置
    # frame.pack()
    return frame