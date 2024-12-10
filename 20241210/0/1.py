def subr():
    yield "One"
    yield "Two"

def task():
    for i in range(3):
        yield from subr()
        yield f"{i} Pass"

for res in task():
    print(res)