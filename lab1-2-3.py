import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk

import warnings
warnings.filterwarnings('ignore')

def run():
    root = Tk()
    root.title("Приложение на Tkinter")
    root.geometry("300x250")
    btn = ttk.Button(text="Данные из файла", command=file_read)
    btn.pack()

    btn = ttk.Button(text="Данные функции", command=func_read)
    btn.pack()

    btn = ttk.Button(text="Решение нелин. ур (Дихотомия)", command=dichotomy_setting)
    btn.pack()

    btn = ttk.Button(text="Оптимизация функции (Золотое сечение)", command=golden_setting)
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
    x=np.linspace(-10,10,10001)
    y=func(x)
    plt.close()
    d = 1
    plt.plot(x, y)

    if axis:
        plt.axhline(0, color='black')
        plt.axvline(0, color='black')

    if len(coo) > 0:
        plt.plot(coo[0], coo[1], 'ro', label=f"На [{line[0]}, {line[1]}]:\nx = {coo[0]:.6f}\nf(x)={coo[1]:.6f}")
    
    if len(line) > 0:
        plt.axvline(line[0], ls='--', color='red')
        plt.axvline(line[1], ls='--', color='red')

    plt.legend(loc='upper left')
    plt.grid(True)
    plt.show()

def dichotomy(f, a, b, epsilon=1e-6, max_iter=100):

    if f(a) * f(b) >= 0:
        raise ValueError("Функция должна существовать и иметь разные знаки на концах интервала")
    
    print(f"{'Итерация':<10} {'a':<12} {'b':<12} {'c':<12} {'f(c)':<12} {'Погрешность':<12}")
    print("-" * 70)
    
    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        
        error = (b - a) / 2
        
        print(f"{i+1:<10} {a:<12.6f} {b:<12.6f} {c:<12.6f} {fc:<12.6f} {error:<12.6f}")
        
        if abs(fc) < epsilon or error < epsilon:
            return c
        
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    
    return (a + b) / 2

def dichotomy_setting():
    error = 1e-4
    a = 9.2
    b = 9.7

    print("\nДихотомия")
    print("=" * 60)

    root = dichotomy(f, a, b, epsilon=error)

    # print(f"\nНайденный корень: {root:.6f}")
    # print(f"\nТочность: {error:.4f}, Интервал = [{a}, {b}]")
    # print(f"Проверка: f({root:.6f}) = {f(root):.6f}")

    coo = (root, f(root))
    line = (a, b)

    func_read(f, coo=coo, line=line, axis=True)

def golden(f, a, b, tol=1e-6, max_iter=100, find_min=True):
    
    phi = (1 + np.sqrt(5)) / 2

    if not find_min:
        original_f = f
        f = lambda x: -original_f(x)
    
    
    print(f"{'Итерация':<8} {'a':<12} {'b':<12} {'x1':<12} {'x2':<12} {'f(x1)':<12} {'f(x2)':<12} {'Длина инт.':<12}")
    print("-" * 100)
    
    for i in range(max_iter):
        L = b - a
        x1 = b - L / phi
        x2 = a + L / phi
        
        f1 = f(x1)
        f2 = f(x2)
        
        print(f"{i+1:<8} {a:<12.6f} {b:<12.6f} {x1:<12.6f} {x2:<12.6f} "
              f"{f1:<12.6f} {f2:<12.6f} {L:<12.6f}")
        
        if L < tol:
            break
        
        if f1 < f2:
            b = x2
        else:
            a = x1
    
    extremum_point = (a + b) / 2
    extremum_value = f(extremum_point)
    
    if not find_min:
        extremum_value = -extremum_value
    
    return extremum_point, extremum_value

def golden_setting():
    a, b = 2.25, 3.15
    find_min = True
    error = 1e-4

    print("\nЗолотое сечение")
    print("=" * 60)

    extremum_point, extremum_value = golden(
        f, a, b, tol=error, find_min=find_min
    )

    coo = (extremum_point, extremum_value)
    line = (a, b)

    # print(f"\nТочность: {error:.4f}, Интервал = [{a}, {b}]")
    # print(f"Точка экстремума: x = {extremum_point:.8f}")
    # print(f"Значение функции: f(x) = {extremum_value:.8f}")

    func_read(f, coo=coo, line=line, axis=True)

if __name__ == "__main__":
    run()