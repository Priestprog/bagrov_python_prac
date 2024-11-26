import binascii
with open("text-6", "rb") as f:
   data = f.read()
print(binascii.hexlify(data))

print(binascii.hexlify(data, " ",4).split())
for adr, i in enumerate(range(0, len(data), 4)):
    print(f"{adr:08x}  :{data[i:i+4]}")