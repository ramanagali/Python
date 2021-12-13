# computes Lowest Common Multiple (LCM) / Least Common Denominator (LCD)
# useful for adding and subtracting fractions

# 2 numbers


def lcm(num1, num2):
    # 12,8 => 8,12
    if num1 > num2:
        num1, num2 = num2, num1

    # find all factors of num1 and num2
    for x in range(num2, num1 * num2 + 1, num2):
        if x % num1 == 0:
            return x


def lcm3(nums):
    nums.sort()
    worst = nums[0]*nums[1]*nums[2]

    for x in range(nums[2], worst + 1, nums[2]):
        if x % nums[0] == 0 and x % nums[1] == 0:
            return x

# best solution by GVR


def find_lcm(x, y):
    if x > y:
        larger = x
    else:
        larger = y

    while True:
        if (larger % x == 0) and (larger % y == 0):
            lcm = larger
            break
        larger = larger * 2
    return lcm


if __name__ == '__main__':
    val = find_lcm(24, 36)
    print('LCM of =', val)

    nums = [3, 2, 16]
    print('LCM of 3,2,16=', str(lcm3(nums)))
