from fractions import Fraction as frac

def fun(s,w,ka,la,kb,lb):
    j = 0
    sum1 = 0
    for el1 in la:
        sum1 += el1*(s**j)
        j+=1
    j = 0
    sum2 = 0
    for el2 in lb:
        sum2 += el2*(s**j)
        j+=1
    return True if sum1/sum2 == w else False


l = list(map(frac, input().split(", ")))
s, w, kA = l[0:3]
lA = l[3:4+int(kA)]
kB = int(l[4+int(kA)])
lB = l[5+int(kA):]

print(fun(s,w,kA,lA,kB,lB))



