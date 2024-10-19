text = input().lower()
pairs = set()
for i in range(len(text) - 1):
    if text[i].isalpha() and text[i + 1].isalpha():
        pairs.add(text[i:i + 2])
print(len(pairs))