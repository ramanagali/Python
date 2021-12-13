
def find_sum(n):
    if n == 1:
        return 1
    return n + find_sum(n-1)


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


# print fibonacci numbers up to
def print_fibonacci(n):
    fib = []
    for i in range(n):
        if i <= 1:
            fib.append(i)
        else:
            fib.append(i-1 + i-2)
    print(fib)


def fibonacci_series_recursion(n):
    if n <= 1:
        return n
    return (fibonacci_series_recursion(n-1) + fibonacci_series_recursion(n-2))


if __name__ == '__main__':
    # print(find_sum(7))
    # 0,1,1,2,3,5,8,13,21,34,55 <-- fibonacci numbers
    # 0,1,2,3,4,5,6,7,8,9 <-- index

    num = int(input("Enter a number: "))
    for i in range(num):
        print(fibonacci_series_recursion(i))
    print(f'Fibonacci number for {num} is: ', fibonacci(num))
