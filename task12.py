print("Введите координаты точки A")
x1 = float(input())
y1 = float(input())
print("Введите координаты точки B")
x2 = float(input())
y2 = float(input())

if abs(y2-0)/abs(x2-0) < abs(y1-0)/abs(x1-0):
    print("OA образует больший угол с осью OX, чем OB")
elif(abs(y2-0)/abs(x2-0) > abs(y1-0)/abs(x1-0)):
    print("OB образует больший угол с осью OX, чем OA")
else:
    print("OA и OB образуют одинаковый угол с осью OX")