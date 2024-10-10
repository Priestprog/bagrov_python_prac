l = list()
kolvo_gaza = kolvo_zizi  = 0
while s := input():
    if s[1] == ".":
        kolvo_gaza += 1
    elif s[1] == "~":
        kolvo_zizi += 1
    else:
        width = len(s)
height = kolvo_zizi + kolvo_gaza + 2
V_gaza = kolvo_gaza * (width-2)
V_zizi = kolvo_zizi * (width-2)
V = V_zizi + V_gaza

print("#" * height)
for i in range(V_gaza//(height-2)):
    print("#", "." * (height-2), "#", sep="")
if (V_zizi % (height-2)) != 0:
    strok_zizi = V_zizi//(height-2) + 1
    V_zizi = (V_zizi//(height-2) + 1)* (height-2)
    V_gaza = V - V_zizi
else:
    strok_zizi = V_zizi // (height - 2)
for j in range(strok_zizi):
    print("#", "~" * (height-2), "#", sep="")
print("#" * height)

vmax = max(V_gaza, V_zizi)
print(f"{"."*V_gaza}{" " * (vmax - V_gaza)} {V_gaza}/{V}")
print(f"{"~"*V_zizi}{" " * (vmax - V_zizi)} {V_zizi}/{V}")

"""
########
#......#
#~~~~~~#
#~~~~~~#
########
"""


"""
#########
#.......#
#~~~~~~~#
#~~~~~~~#
#########
"""

"""
##########
#........#
#~~~~~~~~#
#~~~~~~~~#
##########
"""