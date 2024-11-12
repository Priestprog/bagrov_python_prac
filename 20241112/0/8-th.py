from math import inf

def divisor(a, b):
    if round(b,2) == 0:
        raise ValueError("Division by zero")
    c = a / b
    return -c

def proxy(fun, *args):
    try:
        return fun(*args)
    except ZeroDivisionError:
        return inf
    except ValueError as V:
        print(V)
        return -inf

for i in range(-2, 3):
    print(proxy(divisor, 100, i))

print(divisor(12,0.00045))