from math import *
def S(f,g):
    def fun(x):
        return f(x) + g(x)
    return fun


def SS(*f):
    def fun(x):
        return min(func(x) for func in f)
    return fun

from math import *
def SSS(*funs):
    return lambda x: min(f(x) for f in funs )


res = S(sin,cos)
res2 = SS(sin, cos, tan)
print(res(pi/4))
print(res2(pi/2))
