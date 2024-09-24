a = [[1,2,3],[4,5,6],[2,3]]
b=[]
while a := input():
    b.append(eval(a))

print(b)
print()

for i in range(1, len(b)):
    for j in range(0, len(b)):
        b[i][j], b[j][i] = b[j][i], b[i][j]
print(b)
