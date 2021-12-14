def mySqrt(x):

    r = x
    precision = 10 ** (-10)
    print(precision)
    while abs(x - r * r) > precision:
        r = (r + x / r) / 2

    return r


print(mySqrt(25))
print(mySqrt(36))
