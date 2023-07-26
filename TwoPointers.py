
class Solution:
    # 283. Move Zeroes

    def moveZeroes(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        start, end = 0, len(nums) -1
        while start < end:
            if nums[start] == 0:
                nums.pop(start)
                nums.append(0)
                end -= 1
            else:
                start += 1
        return nums
        