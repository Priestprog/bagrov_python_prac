from math import *



W=100
H=50
A, B = -4, 4
for i in range(H):
    x = (B-A)/(H-1) * i +A
    y = sin(x)
    shift = round((y+1)/2 *W)
    print(" " * shift, "*")

