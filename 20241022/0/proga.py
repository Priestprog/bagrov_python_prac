from itertools import *
def fun(n):
    sum = 0
    for i in range(1,n+1):
        sum += 1/(i**2)
        yield sum

res = fun(10)
print(list(res))

res = accumulate([1/i**2 for i in range(1, 10000)])
print(list(res)[-1])

res_sum = sum([1/i**2 for i in range(1, 10000)])
print(res_sum)

ge = ((i*2 + 1 ) % 7 for i in range(30))
print(ge)