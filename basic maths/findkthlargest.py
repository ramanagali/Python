
class Solution:
    # O(nlgn) time
    def findKthLargest1(self, nums, k):
        return sorted(nums, reverse=True)[k-1]

    # O(n) time, quick selection
    def findKthLargest(self, nums, k):
        # convert the kth largest to smallest
        return self.findKthSmallest(nums, len(nums)+1-k)

    def findKthSmallest(self, nums, k):
        if nums:
            pos = self.partition(nums, 0, len(nums)-1)
            if k > pos+1:
                return self.findKthSmallest(nums[pos+1:], k-pos-1)
            elif k < pos+1:
                return self.findKthSmallest(nums[:pos], k)
            else:
                return nums[pos]

    # choose the right-most element as pivot
    def partition(self, nums, l, r):
        low = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low


nums = [71, 34, 0, 36, 26, 15, 3, 69, 93, 85]
print('Sorted', sorted(nums))
obj = Solution()
print(obj.findKthLargest1(nums, 1))
print(obj.findKthLargest1(nums, 2))
print(obj.findKthLargest1(nums, 3))
print(obj.findKthLargest1(nums, 9))
print(obj.findKthLargest1(nums, 10))
