while s := input():
    print(s.encode('latin1',errors="replace").decode('cp1251'))
