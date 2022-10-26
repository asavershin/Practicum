print("Введите количество камней")
n = int(input())
print('Введите вес камней')
stones = list()
for i in range(n):
    stones.insert(i, int(input()))
stones = sorted(stones, reverse=True)
for i in stones:
    print(i)
stones1 = list()
stones2 = list()
sum1, sum2 = 0, 0
flag = True
for i in stones:
    if sum1 <= sum2:
        stones1.append(i)
        sum1 += i
    elif sum2 <= sum1:
        stones2.append(i)
        sum2 += i
if max(sum1,sum2)/min(sum1, sum2) <= 2:
    print("Разделили камни на две группы")
    print("Первая группа:", end='')
    for i in stones1:
        print(i, end=' ')
    print()
    print("Вторая группа:", end='')
    for i in stones2:
        print(i, end=' ')
else:
    print("Камни не получилось разделить")
