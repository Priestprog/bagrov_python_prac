from collections import UserString
class DivStr(UserString):
    def __init__(self, s=""):
        super().__init__(s)
    def __floordiv__(self, n):
        if not self.data:
            return iter([])
        part_size = len(self.data) // n
        return iter([self.data[i * part_size: (i + 1) * part_size] for i in range(n)])
    def __mod__(self, n):
        if not self.data:
            return DivStr("")
        return DivStr(self.data[n * (len(self.data) // n):])

import sys
exec(sys.stdin.read())
