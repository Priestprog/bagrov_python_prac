def fun(a:int, b: str) -> str:
    return a*b

print(fun(12, "sdfsdf"))
print(fun(12, 23))
print(fun(2, 1.1))

print(fun.__annotations__)


class C:
    a: int = 100500
    b: float


print(C.__annotations__)


class A:
    a: int
    def __init__(self, val):
        typ = self.__annotations__["a"]
        if typ == type(val):
            self.a = val
        print(typ)
a = A(123)
print(a.a)