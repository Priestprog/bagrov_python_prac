from collections import Counter
from timeit import Timer


def fun1(s):
    slov = {el: 0 for el in s}
    for el in s:
        slov[el] += 1
    return slov

def fun2(s):
    return Counter(s)

s = "word word neword".split()
f1 = fun1(s)
f2 = fun2(s)

T1 = Timer("fun1(s)", globals=globals())
T2 = Timer("fun2(s)", globals=globals())

print("for: ", T1.autorange(),"\ncounter: ",  T2.autorange())

#1
slov = {el:0 for el in s}
for el in s:
    slov[el] +=1
print(slov)


#2
print(Counter(s))


#однострочник
sr = "sdfsdfsd fs df sdf s df sd fs d f sf sd f s fsdfsdfsdf sd fs df"
print(" ".join({el:0 for el in (sr.split())}))

