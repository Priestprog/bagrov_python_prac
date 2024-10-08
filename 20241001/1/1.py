def Pareto(*list_of_pairs):
    list_of_pareto = list()
    length_of_list = range(len(list_of_pairs))
    for i in length_of_list:
        flag = 1
        for j in length_of_list:
            if list_of_pairs[i][0] <= list_of_pairs[j][0] and list_of_pairs[i][1] <= list_of_pairs[j][1] and any([list_of_pairs[i][0]< list_of_pairs[j][0], list_of_pairs[i][1]< list_of_pairs[j][1]]):
                flag = 0
        if flag:
            list_of_pareto.append(list_of_pairs[i])

    return tuple(list_of_pareto)


import sys
exec(sys.stdin.read())