from math import *

def show(screen):
    print("\n".join(["".join(s) for s in screen]))


def scale(a, b, A, B, x):
    return (B-A) * (x-a) / (b-a) + A


def gra(w, h, a, b, func):
    l = [[" "] * w for j in range(h)]
    s = 0
    values = []
    min, max = inf, -inf
    for i in range(w):
        x = scale(0,w-1,a,b,i)
        y = - eval(func)
        values.append((i,y))
        if y > max:
            max = y
        if y < min:
            min = y


    for eli,ely in values:
        s_pred = s
        s = round(scale(min,max,0,h-1,ely))
        l[s][eli] = "*"
        if  s_pred > s:
            for k in range(s+1,s_pred):
                l[k][eli-1] = "*"
        elif s > s_pred and eli!=0:
            for e in range(s_pred+1,s):
                l[e][eli-1] = "*"
    show(l)

w,h,a,b,func = input().split(" ")
w, h, a, b = eval(f"{w}, {h}, {a}, {b}")
gra(w,h,a,b,func)

