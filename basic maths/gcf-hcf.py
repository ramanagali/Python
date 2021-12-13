# computes Greatest Common Factor GCF / Greatest Common Divisor GCD of two numbers
# useful for reducing fractions


def gcf(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1

    for x in range(num1, 0, -1):
        if num1 % x == 0 and num2 % x == 0:
            return x

# Python program to find H.C.F of two numbers
# define a function


def compute_hcf(x, y):

    # choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x

    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf


for x in range(25, 0, -1):
    print(x)

# print("The H.C.F. is", str(compute_hcf(18, 204)))
# print("The H.C.F. is", str(compute_hcf(25, 125)))
# print("The H.C.F. is", str(compute_hcf(54, 24)))
