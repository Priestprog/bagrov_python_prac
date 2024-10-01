def F(a,b):
    def fun(x):
        return a*x+b

    return fun


res = F(10,5)
print(res(2))