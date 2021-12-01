
def find_sum(n):
    if n == 1:
        return 1
    return n + find_sum(n-1)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# print fibonacci numbers up to n


if __name__ == '__main__':
    print(find_sum(7))
    # 0,1,1,2,3,5,8,13,21,34,55 <-- fibonacci numbers
    # 0,1,2,3,4,5,6,7,8,9 <-- index
    print(fibonacci(10))
