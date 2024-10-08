from math import *

def show(screen):
    print("\n".join(["".join(s) for s in screen]))


def scale(a, b, A, B, x):
    return (B-A) * (x-a) / (b-a) + A

def gra(a,b,w,h):
    l = [[" "] * w for  j in range(h)]
    for i in range(w):
        x = scale(0,w-1,a,b,i)
        y = sin(x)
        s = scale(-1,1,0,h-1,y)
        l[round(s)][i] = "*"

    show(l)

print(gra(-4,4,100,20))
