class Vowel:
    __slots__ = ('a', 'e', 'i', 'o', 'u', 'y', '_full')
    answer = 42

    def __init__(self, **kwargs):
        for key in kwargs:
            if key not in self.__slots__:
                raise AttributeError(f"Invalid slot: {key}")
            setattr(self, key, kwargs[key])
            self._full = all(hasattr(self, slot) for slot in self.__slots__[:-2])
    def __str__(self):
        fields = sorted((k, getattr(self, k)) for k in self.__slots__[:-2] if hasattr(self, k))
        return ', '.join(f"{key}: {value}" for key, value in fields)

    @property
    def full(self):
        return all(hasattr(self, slot) for slot in self.__slots__[:-2])

    @full.setter
    def full(self, value):
        pass

import sys
exec(sys.stdin.read())