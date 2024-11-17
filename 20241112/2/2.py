class InvalidInput(Exception): pass
class BadTriangle(Exception): pass
def triangleSquare(inStr):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(inStr)
    except:
        raise InvalidInput("Invalid input")
    try:
        area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        if area == 0:
            raise BadTriangle("Not a triangle")
        return round(area, 2)
    except:
        raise BadTriangle("Not a triangle")

while True:
    try:
        inStr = input()
        area = triangleSquare(inStr)
        print(f"{area:.2f}")
        break
    except (InvalidInput, BadTriangle) as error:
        print(error)
