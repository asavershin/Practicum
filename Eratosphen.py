#алгоритм Эратосфена
# Вывести простые числа от A  до B читаемые из файла
inFile = open('in.txt', 'r')
data = []
for line in inFile:
    data.append([int(x) for x in line.split()])

n=data[0][1]

a = []
for i in range(n + 1):
    a.append(i)
a[1] = 0
i = 2
while i <= n:
    if a[i] != 0:
        j = i + i
        while j <= n:
            a[j] = 0
            j = j + i
    i += 1

out = open('out.txt','w')
for i in range(n + 1):
    if a[i] != 0 and a[i] > data[0][0]:
        print(str(a[i]), file = out, end = ' ')

out.close()
inFile.close()
