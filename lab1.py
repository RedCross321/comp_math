import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
import math 

# import warnings
# warnings.filterwarnings('ignore')


def run():
    root = Tk()
    root.title("Приложение на Tkinter")
    root.geometry("300x250")
    btn = ttk.Button(text="Данные из файла", command=file_read)
    btn.pack()

    btn = ttk.Button(text="Данные функции", command=func_read)
    btn.pack()

    Button(root, text="Закрыть", command=root.destroy).pack()
    root.mainloop()

def f(x):
    return (x - 1.5) * (np.sin(2*np.pi*x) / (x - 2))

def file_read():
    X = []
    Y = []

    with open("func.txt", 'r') as f:
        num = f.read().splitlines()
    for n in num[1:]:
        X.append(float(n.split()[0]))
        Y.append(float(n.split()[1]))

    plt.close()
    plt.plot(X, Y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

def func_read(func = f, coo = (), line = (), axis=False):
    x=np.linspace(-10,10,101)
    y=func(x)
    plt.close()

    plt.plot(x, y)

    if axis:
        plt.axhline(0, color='black')
        plt.axvline(0, color='black')

    if len(coo) > 0:
        plt.plot(coo[0], coo[1], 'ro')
    
    if len(line) > 0:
        plt.axvline(line[0], ls='--', color='red')
        plt.axvline(line[1], ls='--', color='red')

    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    run()