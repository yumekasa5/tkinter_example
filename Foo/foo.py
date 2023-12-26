import numpy as np
import matplotlib.pyplot as plt

def foo():
    print('Foo')
    
class MakeGraph:
    def __init__(self):
        self.x = np.array([i for i in range(1000)])
        self.y = 20 * self.x + 100
        
    def make_graph(self):
        fig, ax = plt.subplots()
        ax.plot(self.x, self.y, label='cx_Freeze')
        ax.legend()
        plt.savefig('cx_FreezeImage.png')