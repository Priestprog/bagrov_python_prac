def minus(arg1, arg2):
    if type(arg1) == type(arg2):
        if type(arg1) in [tuple, list]:
            res = list()
            type_of_args = type(arg1)
            for i in range(len(arg1)):
                flag = 1
                for j in range(len(arg2)):
                    if arg1[i] == arg2[j]:
                        flag = 0
                if flag:
                    res.append(arg1[i])
            return type_of_args(res)
        else:
            return arg1-arg2

import sys
exec(sys.stdin.read())