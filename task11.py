print("Введите систему счисления, число и делитель")
k = int(input())
m = int(input())
num = input()

sum = 0
len = len(num)
for i in range(len):
    sum = (sum + int(num[len - 1 - i])*k**i) % m
print(f"Остаток от деления числа {num} в {k} на {m} равна {sum % m}")
