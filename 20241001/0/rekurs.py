def fun(n, res=[1]):
    if len(res) == n:
        print(*res, sep="")
    else:
        fun(n, res + [0])
        fun(n, res + [1])


fun(4)