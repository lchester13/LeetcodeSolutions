

class Solution:

    # 215. Kth Largest Element in an Array
    # Quick Select 
    def findKthLargest(nums, k):
        n = len(nums)
        pivot = n // 2 - 1 
        left = 2*pivot + 1
        right = 2*pivot + 2
        print(nums[pivot], nums[left], nums[right])

    nums = [3,2,1,5,6,4] 
    k = 2
    findKthLargest(nums, k)