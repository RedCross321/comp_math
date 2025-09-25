import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import numpy as np
from tkinter import *

root = tk.Tk()
root.title("Решение СЛАУ 5x4")
root.geometry("600x400")

main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

headers = ["x1", "x2", "x3", "x4"]
for col, header in enumerate(headers):
    ttk.Label(main_frame, text=header, font=("Arial", 12, "bold")).grid(
        row=1, column=col, padx=5, pady=5)

entries = []
for row in range(4):
    row_entries = []
    for col in range(4):
        entry = ttk.Entry(main_frame, width=8, font=("Arial", 10))
        entry.grid(row=row+2, column=col, padx=5, pady=2)
        row_entries.append(entry)
    
    ttk.Label(main_frame, text="=").grid(row=row+2, column=5, padx=5)
    
    free_entry = ttk.Entry(main_frame, width=8, font=("Arial", 10))
    free_entry.grid(row=row+2, column=6, padx=5, pady=2)
    row_entries.append(free_entry)
    
    entries.append(row_entries)

default_values = [
    [2.56, 1.34, 0.78, -3.21, 5.9],
    [4.12, -0.89, -1.23, 5.43, 7.36],
    [-3.05, 2.77, 1.98, 4.16, 4.81],
    [6.72, 8.55, -9.41, -2.03, -1.28]
]

for i, row in enumerate(default_values):
    for j, value in enumerate(row):
        entries[i][j].delete(0, tk.END)
        entries[i][j].insert(0, str(value))

def solve():
    new = []
    for row in range(4):
        for col in range(4):
            new.append(float(entries[row][col].get()))

    matrix = np.array(new).reshape(4,4)
    n = matrix.shape[0]

    # if matrix.shape[0] != matrix.shape[1]:
    #     raise ValueError("Матрица не квадратная")

    det = 1.0
    for i in range(n):
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k, i]) > abs(matrix[max_row, i]):
                max_row = k

        if abs(matrix[max_row, i]) < 1e-12:
            return 0.0
        
        if max_row != i:
            matrix[[i, max_row]] = matrix[[max_row, i]]
            det *= -1
        
        det *= matrix[i, i]

        for k in range(i + 1, n):
            factor = matrix[k, i] / matrix[i, i]
            matrix[k, i:] -= factor * matrix[i, i:]

    showinfo(title="Определитель матрицы", message=f"Определитель матрицы = {det}")

    # print(matrix)
def not_my():
    new = []
    for row in range(4):
        for col in range(4):
            new.append(float(entries[row][col].get()))

    matrix = np.array(new).reshape(4,4)
    print(np.linalg.det(matrix))

button_frame = ttk.Frame(main_frame)
button_frame.grid(row=6, column=0, columnspan=7, pady=20)

ttk.Button(button_frame, text="Решить", 
            command=solve).pack(side=tk.LEFT, padx=10)

button_frame = ttk.Frame(main_frame)
button_frame.grid(row=7, column=0, columnspan=7, pady=20)

ttk.Button(button_frame, text="Решить", 
            command=not_my).pack(side=tk.LEFT, padx=30)

button_frame = ttk.Frame(main_frame)
button_frame.grid(row=8, column=0, columnspan=7, pady=20)

ttk.Button(button_frame, text="Закрыть", 
            command=root.destroy).pack(side=tk.LEFT, padx=30)
root.mainloop()