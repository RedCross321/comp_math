import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Приложение на Tkinter")
root.geometry("300x250")

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

def f(x):
    return (x - 1.5) * (np.sin(2*np.pi*x) / (x - 2))

def func_read():
    x=np.linspace(-10,10,101)
    y=f(x)
    plt.close()
    plt.plot(x, y)
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()


btn = ttk.Button(text="Данные из файла", command=file_read)
btn.pack()

btn = ttk.Button(text="Данные функции", command=func_read)
btn.pack()

Button(root, text="Закрыть", command=root.destroy).pack()
root.mainloop()