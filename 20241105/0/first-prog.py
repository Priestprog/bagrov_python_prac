class C:
    pass

C.a = 123
e = C()
C.qwerty  =100500
print(e.qwerty)

def fun(a,b):
    print(a,b)

C.foo = fun
print(C.foo(1,2))
