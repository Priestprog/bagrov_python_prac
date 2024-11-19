class Istype:
    def __init__(self, typ):
        self.typ = typ

    def __call__(self, fun):
        def newfun(*args):
            for arg in args:
                if not isinstance(arg, self.typ):
                    raise TypeError("Wrong type")
            print(fun(*args))
            return fun(*args)
        return newfun
@Istype(int)
def foo(a, b, c, d):
    return a + b + c + d
foo(1, 2, 3, 4)
