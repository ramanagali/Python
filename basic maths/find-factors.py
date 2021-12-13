# Python Program to find the factors of a number

# This function computes the factor of the argument passed


def print_factors(x):
    print("The factors of", x, "are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i, end=' ')


num = 320
print_factors(num)
print()
# Take a list of numbers
my_list = [12, 65, 54, 39, 102, 339, 221, ]

# use anonymous function to filter
result = list(filter(lambda x: (x % 13 == 0), my_list))

# display the result
print("Numbers divisible by 13 are", result)
