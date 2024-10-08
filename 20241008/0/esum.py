from fractions import Fraction
from decimal import Decimal
from decimal import getcontext

def esum(N, one):
    numb = one
    e =one
    for i in range(1,N):
        numb /= i
        e+=numb
    return e


getcontext().prec = 100
print(esum(1000,Decimal("1")))
print(esum(100,1))