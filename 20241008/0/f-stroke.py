w = len(f"{12:b} = {24:x}")
for i in range(12,24):
    mw = len(f"{i:b} = {i:x}")
    print(f"{i:b} {"=":{w-mw+1}} {i:x}")