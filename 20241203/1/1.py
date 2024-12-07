class dump(type):
    def __new__(cls, name, parents, namespace):
        for attr_name, attr_value in namespace.items():
            if callable(attr_value):
                def wrapper(func):
                    def wrapped(self, *args, **kwargs):
                        print(f"{func.__name__}: {args}, {kwargs}")
                        return func(self, *args, **kwargs)
                    return wrapped

                namespace[attr_name] = wrapper(attr_value)
        return super().__new__(cls, name, parents, namespace)

import sys
exec(sys.stdin.read())
