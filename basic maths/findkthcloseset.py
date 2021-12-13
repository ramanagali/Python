def findClosestElements(arr, k, x):
    """
    :type arr: List[int]
    :type k: int
    :type x: int
    :rtype: List[int]
    """
    lo, hi = 0, len(arr)-k
    while lo < hi:
        mid = (lo + hi)//2
        if x-arr[mid] > arr[mid+k]-x:
            lo = mid + 1
        else:
            hi = mid
    return arr[lo:lo+k]


class Solution(object):
    def findClosestElements(self, arr, k, target):
        l = r = self.binary_search(arr, target)
        while r - l < k:
            if r >= len(arr) or l > 0 and target - arr[l - 1] <= arr[r] - target:
                l -= 1
            else:
                r += 1
        return arr[l:r]

    def binary_search(self, arr, target):
        l, r = 0, len(arr) - 1
        while l + 1 < r:
            mid = (l + r) // 2
            if arr[mid] == target:
                return mid
            if arr[mid] < target:
                l = mid
            else:
                r = mid
        # Post
        if arr[l] > target:
            return l
        if arr[l] == target:
            return l
        if arr[l] < target < arr[r]:
            return l + 1
        if arr[r] == target:
            return r
        if arr[r] < target:
            return r + 1


arr = [1, 2, 3, 4, 5],
k = 4
x = 3
obj = Solution()
res = findClosestElements(arr, k, x)
print(res)
# Output: [1, 2, 3, 4]

arr = [2, 4, 5, 6, 9]
k = 3
x = 6
res = findClosestElements(arr, k, x)
print(res)
# Output: [4, 5, 6]
