def f(x):
    yield ">"
    yield from x
    yield "<"
    return len(x)

def po_kochkam(n):
    for i in range(n):
        yield "по кочкам"
    return "и в яму"

def fun(n):
    s = yield from po_kochkam(n)
    yield s


g = f("10")
print(next(g))
print(next(g))
print(next(g))
print(next(g))


p = fun(3)
res = list(p)
print(res)
