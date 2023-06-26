
class LeetCodeSolutions:
    
    #35. Search Insert Position

    def searchInsert(self, nums, target):
        """
        Given a sorted array of distinct integers and a target value, 
        return the index if the target is found. 
        If not, return the index where it would be if it were inserted in order.
        """
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (high + low) // 2

            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                low = mid+1
            else:
                high = mid-1
            
        return low

    

            