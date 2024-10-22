from itertools import *
def fun(n):
    sum = 0
    for i in range(1,n+1):
        sum += 1/(i**2)
        yield sum


def fun2(n):
    print(list(filterfalse(lambda x: x % n, [i for i in range(12, 100, 5)])))

def fun3(seq, n):
    yield from chain.from_iterable(map(lambda  x: repeat(x,n), seq))



print([f"{v}{g}" for v, g in list(product("abcdefgh", range(1,9)))])

print(list(fun3([1,2], 2)))



print(list(dropwhile(lambda x: x < 1.6, list(fun(50))))[:10])

fun2(3)

