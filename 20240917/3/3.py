n = int(input())
i = j = n
summa = 0
while i < n+3:
    while j < n+3:
        print(i,"*",j,"=", sep = " ", end= " ")
        x = y = i * j
        while y > 0:
            summa += y % 10
            y = y // 10
        if  summa == 6:
            print(":=)", end= " ")
        else:
            print(x, end= " ")
        summa = 0
        j += 1
    print("")
    j -= 3
    i += 1

