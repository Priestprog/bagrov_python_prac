
def pgen():
    print(":: ")
    res = yield "Start"
    print("> ")
    while res := (yield f"/ {res} /"):
        print(">> ")
    yield "Finish"
    print("< ")

g = pgen()
print(next(g))
print(g.send("!@#"))
s = g.send("87979")
print(next(g))

s = pgen()
next(s)
for i in range(5,1,-1):
    print(s.send(i))


