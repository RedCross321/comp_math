import numpy as np
import matplotlib.pyplot as plt
import lab1

def golden_section_search(f, a, b, tol=1e-6, max_iter=100, find_min=True):
    
    phi = (1 + np.sqrt(5)) / 2
    print(phi)
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

def f(x):
    return (x - 1.5) * (np.sin(2*np.pi*x) / (x - 2))

a, b = 2.25, 3.15
find_min = True
error = 1e-4

extremum_point, extremum_value = golden_section_search(
    f, a, b, tol=error, find_min=find_min
)

coo = (extremum_point, extremum_value)
line = (a, b)


print(f"\nТочность: {error:.4f}, Интервал = [{a}, {b}]")
print(f"Точка экстремума: x = {extremum_point:.8f}")
print(f"Значение функции: f(x) = {extremum_value:.8f}")

lab1.func_read(f, coo=coo, line=line, axis=True)
