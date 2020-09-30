def ft_straight_code(a):
    if a > 0:
        p = ''
        while a > 0:
            s = str(a % 2)
            p = s + p
            a = int(a / 2)
        while len(p) != 8:
            p = '0' + p
        return p
    else:
        a = -a
        n = ''
        while a > 0:
            s = str(a % 2)
            x = s + x
            a = int(a / 2)
        while len(n) != 7:
            x = '0' + x
        x = '1' + x
    return x
