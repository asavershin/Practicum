
a = float(input())
b = float(input())
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

if a*x1+b <= y1 and a*x2+b >= y2 or a*x2+b <= y2 and a*x1+b >= y1:
    print(f"Прямая y = {a}x + {b}  пересекает отрезок с концами ({x1},{y1}), ({x2},{y2})")
else:
    print(f"Прямая y = {a}x + {b}  не пересекает отрезок с концами ({x1},{y1}), ({x2},{y2})")