class Singleton(type):
    _instance = []
    _counter = 0
    def __call__(cls, *args, **kw):
        if len(cls._instance) < 2:
             cls._instance.append(super().__call__(*args, **kw))
        cls._counter += 1
        return cls._instance[cls._counter % len(cls._instance)]

class S(metaclass=Singleton):
    A = 3
s, t = S(), S()
s.newfield = 100500
print(f"{s.newfield=}, {t.newfield=}")
print(f"{s is t=}")