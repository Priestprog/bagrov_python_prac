t = "fgdfgdfgdfgd"
match t.split():
    case []:
        print("empty")
    case ["sfsdf"]:
        print("sfsdf")
    case [str(x)]:
        print(x)
    case [x]:
        print(x)
    case [_, *tail]:
        print(tail)

