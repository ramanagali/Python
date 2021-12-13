
def find_sum_of_two(nums, target):
    dic = {}
    for i, num in enumerate(nums):
        if target-num in dic:
            return [dic[target-num], i]
        dic[num] = i


nums = [2, 7, 11, 15]
target = 9
print(find_sum_of_two(nums, target))
# store the target-num in a dictionary
# check if the difference is in the dictionary
