import struct
import random
print(struct.pack("I3si", 123, b"ABC", -8 ))
with open("text-6", "wb") as f:
    for i in range(10):
        f.write(struct.pack("f3si",random.random(), bytes((random.randrange(2,5), random.randrange(2,5), random.randrange(2,5))), random.randrange(25600)))


