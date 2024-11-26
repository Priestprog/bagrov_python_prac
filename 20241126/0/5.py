import pickle
from marshal import dumps

print(pickle.dumps("123456789", protocol=0))
print(pickle.dumps(["123456789", "WER", 5.678], protocol=0).decode())


class C:
    a=1
c = C()
c.b = 123
print(pickle.dumps(c, protocol=0))
dump = pickle.dumps(c, protocol=0)
d = pickle.loads(dump)
print(d.a)
print(d.b)

class SerCls:
    lst = [1,2,3,4,5,5]
    dct = {"a":1, "b":2}
    num = 42
    st = "ljdnfgkljdnjsnd"


ser = SerCls()
dump2 = pickle.dumps(ser, protocol=0)
del ser
print(pickle.loads(dump2))

