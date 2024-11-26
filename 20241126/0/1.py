with open("text", "rb") as f:
    data = f.read()
    print(data)
with open("text", "wb") as f:
    f.write(data[len(data) // 2:] + data[:len(data) // 2])
with open("text", "rb") as f:
    data = f.read()
    print(data)



