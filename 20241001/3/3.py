from math import *
def Calc(s, t ,u):
    def fun(x):
        y = eval(t)
        x = eval (s)
        return eval(u)
    return fun

formula1, formula2, formula3 = eval(input())
x_arg = eval(input())
F = Calc(formula1, formula2, formula3)

print(F(x_arg))