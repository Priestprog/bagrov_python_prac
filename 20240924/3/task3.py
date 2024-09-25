a = list()
a.append(list(map(int,input().split(","))))
l =len(a[0])

for p in range(1,l):
    a.append(list(map(int, input().split(","))))

b = list()
for p in range(l):
    b.append(list(map(int,input().split(","))))

c =[[0 for __ in range(l)] for __ in range(l)]
sum =0
for i in range(l):
    for j in range(l):
        for k in range(l):
            sum += a[i][k]*b[k][j]
        c[i][j] = sum
        sum = 0
    print (*c[i], sep=",")
