sum = 0
while sum <=21:
    n = int(input())
    if n>0:
        sum += n
    else:
        print(n)
        break
else:
    print(sum)
