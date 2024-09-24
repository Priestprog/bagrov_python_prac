a = list(range(5,16))
b = "abcdefghijk"
a[4:8] = list("abcdefghijk")[-5:]
print(a)

c = list(range(5,17))
print(c)
print(c[len(a)//2+1::2][::-1])
print(c[-1: len(a)//2-1:-2])

