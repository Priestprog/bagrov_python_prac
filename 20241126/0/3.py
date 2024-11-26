with open("text2", "r") as f:
    data = f.read()
    print(data)
with open("text2", "w") as f:
    for i in range(len(data) // 3, len(data)):
        if data[i] == "\n":
            break
    print(i)
    f.write(data[:i])
with open("text2", "r") as f:
    data = f.read()
    print(data)
