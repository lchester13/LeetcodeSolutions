
class LeetcodeSolutions:

    #136. Single Number

    def singleNumber(self, nums):
         if len(nums) == 1:
            return nums[0]
         singleNum = 0
         for x in nums:
            #use XOR to get the remaining number
            singleNum ^= x 
         return singleNum

    #169. Majority Element

    def majorityElement(self, nums):
        numTimes = len(nums) // 2
        nums.sort()
        return nums[numTimes]