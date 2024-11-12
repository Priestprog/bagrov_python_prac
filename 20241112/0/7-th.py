while True:
    try:
        a = int(input())
        print(a)
    except Exception:
        print("Error")
    else:
        print("OK")
        break