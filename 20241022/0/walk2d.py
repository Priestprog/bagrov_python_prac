def walk2d():
    x = 0
    y = 0
    para = (x,y)
    while True:
        para = yield (x, y)
        x += para[0]
        y += para[1]


w = walk2d()
next(w)
print(w.send((12,34)))
print(w.send((12,34)))
