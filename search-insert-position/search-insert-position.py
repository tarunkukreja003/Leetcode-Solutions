class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (high + low) // 2
            
            if target < nums[mid]:
                # move left
                if (mid-1 >= low) and (nums[mid - 1] < target):
                    return mid
                high = mid - 1 
                if (mid -1 < low):
                    return low
            
            elif target > nums[mid]:
                # move right
                if (mid+1 <= high) and (nums[mid+1] > target):
                    return mid + 1
                low = mid + 1
                if (mid+1 > high):
                    return mid+1
            
            else:
                return mid