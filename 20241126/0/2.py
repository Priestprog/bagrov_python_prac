with open("0", "rb") as f:
    data = f.read()
    print(data)
with open("0", "wb") as f:
    f.write(data[len(data) // 2:] + data[:len(data) // 2])
with open("0", "rb") as f:
    data = f.read()
    print(data)
