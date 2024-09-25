a = list(map(int,input().split(",")))


b =[]
for el in a:
    b.append(el ** 2 % 100)


for i in range(0, len(b)):
    for j in range(i, len(b)):
        if b[i] > b[j]:
            b[i], b[j], a[i], a[j] = b[j], b[i], a[j], a[i]


print(a)

