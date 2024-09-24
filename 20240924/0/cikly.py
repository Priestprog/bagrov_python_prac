
d = [i*2+1 for i in range(10,20) if i!= 13]
print(d)
start,end = eval(input())
a = [i for i in range(start,end) if i % 2 and "3" not in str(i)]
print(a)