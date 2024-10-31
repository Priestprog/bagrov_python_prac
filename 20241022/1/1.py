def fib(m,n):
    num = 0
    flag = n
    temp1, temp2 = 1, 1
    while True:
        if flag == 0:
            break
        if num >= m:
            yield temp1
            flag -= 1
        tmp = temp1
        temp1 = temp2
        temp2 += tmp
        num += 1

import sys
exec(sys.stdin.read())