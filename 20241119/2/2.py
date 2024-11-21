class Num:
    def __init__(self, n=0):
        self.n = n
        self.values = {}

    def __get__(self, instance, owner):
        return self.values.get(instance, self.n)

    def __set__(self, instance, value):
        if hasattr(value, 'real'):
            self.values[instance] = value.real
        elif hasattr(value, '__len__'):
            self.values[instance] = len(value)
        else:
            self.values[instance] = self.n

import sys
exec(sys.stdin.read())