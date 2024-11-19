def isint(f):
    def funfun(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError("All args must be int")
        return f(*args)
    return funfun

def dumper(f):
    def newfun(*args):
        print(">", *args)
        res = f(*args)
        print("<", res)
        return res
    return newfun

@isint
@dumper
def fun(a,b):
    return a*2+b
print(fun(2,3))
print(fun("sdfsdf",3))