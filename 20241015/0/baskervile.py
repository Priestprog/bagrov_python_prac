from collections import Counter


s = "sdfsdfsdfsdf sdf sdfs df sdf sdfsdfsdf f ghryhtyhj unr fvweq sfvdtbe sdf sdfhy".split()
zap = "f f df unr".split()
cs = Counter(s)
cz = Counter(zap)
if cz-cs:
    print("omagad yes")
else:
    print("nooooo")