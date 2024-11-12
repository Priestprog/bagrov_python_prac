

C = type("C", (), {"a": 100500, "func": lambda self: self.a,
                   "__init__": lambda self, val: setattr(self,"a", val)})
c = C(12)
print(c.func())


class A:
    def fun(self):
        return "A"

class B(A):
    def fun(self):
        return super().fun()+"B"