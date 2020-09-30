import ft_straight_code as pr


def ft_reverse_code(a):
    s = str(pr.ft_straight_code(a))
    g = s[0]
    for i in range(1, len(s)):
        if s[i] == "0":
            g += "1"
        else:
            g += "0"
    return g
