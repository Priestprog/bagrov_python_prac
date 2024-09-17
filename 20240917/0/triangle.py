a,b,c =  eval(input())
if (min(a,b,c) > 0) and (a+b<c or b+c <a or a+c<b):
    print ("yes")
else:
    print("no")
