from timeit import Timer
from string import ascii_lowercase


def unic_lat(s):
    srin = set(s)
    wov = set("aoiuye")
    cons = set(ascii_lowercase) - wov
    return len(srin&wov), len(srin&cons)

s = input()
print(unic_lat(s))
T = Timer(f"unic_lat('{s}')", globals=globals())
print(T.autorange())


s = set(range(1,8))
t = set(range(5,10))

print(s|t)
print(s&t)
print(s^t)
print(s-t)
print(t-s)





""""
s = "aabABbcD123"
gl = set("a", "e", "y", "i", "o", "u")
sogl = set()
for el in s:
    if el.islower() and el.isalpha():
        for el_gl in gl:
            if el_gl

mnv = set(s)
print(mnv)
"""