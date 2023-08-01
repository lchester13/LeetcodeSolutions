

class LeetCodeSolution:


    # 1. Two Sum

    def twoSum(nums, target):
        sumMap = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in sumMap:
                return [sumMap[diff], index]
            sumMap[num] = index
        return

