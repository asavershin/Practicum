
from math import factorial
print("Введите значение K")
k = int(input())
sum = 0
for i in range(k):
    sum = sum + 1/factorial(i+1)
print(sum)