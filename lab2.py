import numpy as np
import lab1

def dichotomy_method(f, a, b, epsilon=1e-6, max_iter=100):

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


def f(x):
    return (x - 1.5) * (np.sin(2*np.pi*x) / (x - 2))

error = 1e-4
a = 0.8
b = 1.8

print(f(a) * f(b) >= 0)
root = dichotomy_method(f, a, b, epsilon=error)

print(f"\nНайденный корень: {root:.6f}")
print(f"\nТочность: {error:.4f}")
print(f"Проверка: f({root:.6f}) = {f(root):.6f}")

coo = (root, f(root))
line = (a, b)

lab1.func_read(f, coo=coo, line=line, axis=True)