from string import ascii_letters
from sys import getsizeof
from pympler import asizeof
class Slotter:
    __slots__ = tuple(ascii_letters)
    def __init__(self):
        for attr in ascii_letters:
            setattr(self, attr, attr)
class Trad:
    def __init__(self):
        for attr in ascii_letters:
            setattr(self, attr, attr)

s = Slotter()
print(s.K)
print(getsizeof(s))
print(getsizeof(Slotter))
print(asizeof.asizeof(s))


t = [Trad() for i in range(1000)]
s = [Slotter() for i in range(1000)]
print(asizeof.asizeof(t))
print(asizeof.asizeof(s))

