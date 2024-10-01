fun = lambda x, y: x*2+y

print(fun(12,23))
print((lambda x, y: x*2+y)(12,23))

print(sorted(range(20),key = lambda x: x%5))

a = list(map(int,input().split(",")))
print(sorted(a,key=lambda x: x**2%100))
