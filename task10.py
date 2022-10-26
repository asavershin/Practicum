#Делится ли двоичное число на 15
print("Введите число в двоичной системе счисления")
num = input()
flag = True
sum = 0
len = len(num)
for i in range(len):
    sum += 2**i*int(num[len - 1 - i]) % 15
if sum % 15 != 0:
    flag = False
if flag:
    print(f"Число {num} делится на 15")
else:
    print(f"Число {num} не делится на 15")
