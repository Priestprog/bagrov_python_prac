class Rectangle:
    rectcnt = 0
    def __init__(self,x1,y1,x2,y2):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.__class__.rectcnt += 1
        setattr(self, f"rect_{self.rectcnt}", self.rectcnt)
    def __str__(self):
        return (f"({self.x1}, {self.y1})   ({self.x1}, {self.y2})    ({self.x2}, {self.y2})   ({self.x2}, {self.y1}) "
                f"\n rectcnt: {self.rectcnt}")
    def __lt__(self, other):
        return (self.x2 - self.x1) * (self.y2 - self.y1) < (other.x2 - other.x1) * (other.y2 - other.y1)
    def __eq__(self, other):
        return (self.x2 - self.x1) * (self.y2 - self.y1) == (other.x2 - other.x1) * (other.y2 - other.y1)
    def __mul__(self, other):
        return self.__class__(self.x1 * other, self.y1 * other, self.x2 * other, self.y2 * other)
    __rmul__ = __mul__
    def __getitem__(self, item):
        return ((self.x1,self.y1), (self.x1,self.y2), (self.x2,self.y2), (self.x2,self.y1))[item]
    def __bool__(self):
        return (self.x2 - self.x1) * (self.y2 - self.y1) != 0
    def __del__(self):
        self.__class__.rectcnt -= 1
        print(self.rectcnt)
r = Rectangle(1,2,3,4)
print(r)
rr = Rectangle(4,2,1,8)
print(rr)
Rectangle.qwe =123
print(r.qwe)
r.qwe = 100500
print(r.qwe)
print(Rectangle.qwe)
del r.qwe
print(r.qwe)

print(rr.__dict__["x1"])

print(r<rr)
print(r*12)
print(12* r)

print(r[1])

if Rectangle(1,1,1,1):
    print("Full")
else:
    print("empty")

