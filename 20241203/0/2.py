class final(type):
    def __new__(metacls, name, parents, namespace):
        if len(parents) > 1:
            raise TypeError(f"Cannot have more than one parent class: {name}")
        return super().__new__(metacls, name, parents, namespace)

class E(metaclass=final): pass
class C(E): pass
#class A(E, int): pass