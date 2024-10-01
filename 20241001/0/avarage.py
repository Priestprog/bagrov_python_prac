def avarage(*b):
    return sum(b)/len(b)

print(avarage(1,2,2,3,4,3,4,))
print(avarage(*range(100)))
