def additional(a):
    b = ""
    if a >= 0:
        while a:
            n = a % 2
            if n == 0:
                b = "0" + b
            else:
                b = "1" + b
            a = a // 2
        while len(b) < 8:
            b = "0" + b
        print(b)

    else:
        a = a * (-1)
        while a:
            n = a % 2
            if n == 0:
                b = "1" + b
            else:
                b = "0" + b
            a = a // 2
        while len(b) < 8:
            b = "1" + b
        print(b)
