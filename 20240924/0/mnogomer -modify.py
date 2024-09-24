a = [[1,2,3],[4,5,6],[2,3]]
b=[]
'''
while a := input():
    b.append(eval(a))
for i in range(0, len(b)):
    print(b[i])
print()
'''
u =[[1,2,3],[4,5,6],[7,8,9]]

g =all([len(u[i]) == len(u) for i in range(0, len(u))])
print(g)

kur =all([len(el) == len(u) for el in u ])
print(kur)

'''
for i in range(1, len(b)):
    for j in range(0, len(b)):
        b[i][j], b[j][i] = b[j][i], b[i][j]

for i in range(0, len(b)):
    print(b[i])
'''