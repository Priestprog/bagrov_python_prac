class A:
    v  = 1

class B(A):
    v = 2


class C:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        return self.__class__(self.val + other.val)

class D(C):
    def __sub__(self, other):
        return self.__class__(self. val - self.other)


print(D(3)+ D(5))

b = B()
b.v = 3
print(b.v)
del b.v
print(b.v)
del B.v
print(b.v)