import numpy as np

class Triangle:
    def __init__(self, p1, p2, p3):
        self.points = np.array([p1, p2, p3], dtype=float)
        self.points = np.hstack((self.points, np.zeros((3, 1))))

    def __abs__(self):
        a, b, c = self.points
        return abs(np.cross(b - a, c - a)[-1]) / 2

    def __bool__(self):
        return bool(not np.isclose(abs(self), 0))

    def __lt__(self, other):
        return bool(abs(self) < abs(other))

    def contains_point(self, point):
        point = np.array([*point, 0])
        a, b, c = self.points
        v1 = np.cross(b - a, point - a)[-1]
        v2 = np.cross(c - b, point - b)[-1]
        v3 = np.cross(a - c, point - c)[-1]
        return (v1 >= 0 and v2 >= 0 and v3 >= 0) or (v1 <= 0 and v2 <= 0 and v3 <= 0)

    def __contains__(self, other):
        if not other:
            return True
        if not self:
            return False
        return all(self.contains_point(pt[:2]) for pt in other.points)

    def __and__(self, other):
        if not self or not other:
            return False
        return any(self.contains_point(pt[:2]) for pt in other.points) or any(other.contains_point(pt[:2]) for pt in self.points)

import sys
exec(sys.stdin.read())