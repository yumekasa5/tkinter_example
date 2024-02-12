# !/usr/bin/python3
# SPDX-FileCopyrightText: 2024 yumekasa5
import numpy as np
import matplotlib.pyplot as plt

    
class MakeGraph:
    def __init__(self):
        self.xdata = np.array([i for i in range(1000)])
        self.ydata = 20 * self.x + 100
        
    def make_graph(self):
        fig, ax = plt.subplots()
        ax.plot(self.xdata, self.ydata, label="sensor data")
        ax.legend()
        plt.savefig('sensor_data.png')