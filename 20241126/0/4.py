s = "Вопрос".encode("cp1251")
s = s.decode("KOI8-R")
print(s)

s = "бМХЛЮМХЕ".encode("Koi8-r")
s = s.decode("cp1251")
print(s)

s = "ОХРЮМХЕ".encode("Koi8-r")
s = s.decode("cp1251")
print(s)