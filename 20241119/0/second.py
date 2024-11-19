def istype(typ):
    def decorator(fun):
        def newfun(*args):
            for arg in args:
                if not isinstance(arg, typ):
                    raise TypeError("Wrong type")
            return fun(*args)
        return newfun
    return decorator

def multicall(times):
    def decorator(fun):
        def newfun(*args):
            return [fun(*args) for i in range(times)]
        return newfun
    return decorator

@istype(int)
@multicall(5)
def simplefun(N):
    return N*2+1

print(*simplefun(4))