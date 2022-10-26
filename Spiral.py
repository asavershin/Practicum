# Вывести в файл кважрат, состоязий из N  на N клеток,
# заполненный числами от 1 до N^2 по спирали против асовой стрелки
print("Введите количество элементов в спирали")
n = int(input())


def spiral(n):
    a = [[0] * n for i in range(n)]
    num = 1
    flag = n**2
    k = 0
    while num <= flag:
        count = k

        while count < n - k and num <= flag:
            a[k][count] = num
            num = num + 1
            count = count + 1
        count = k+1
        while count < n - k and num <= flag:
            a[count][n - k - 1] = num
            num = num + 1
            count = count + 1
        count = n - k - 2
        while count >= k and num <= flag:
            a[n-k-1][count] = num
            num = num + 1
            count = count - 1
        count = n - k - 2
        while count >= k + 1 and num <= flag:
            a[count][k] = num
            num = num + 1
            count = count - 1
        k = k + 1
    return a

out = open('out.txt', 'w')

a = spiral(n)
for i in range(n):
    for k in range(n):
        out.write(str(a[i][k]) + ' ')
    out.write('\n')
out.close()