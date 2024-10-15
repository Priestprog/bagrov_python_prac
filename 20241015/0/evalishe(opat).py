from math import *

s = input()
x,y = eval(input())

print(eval(s,None,{x:"x", y: "y"}))
x,y =y,x
print(eval(s))
