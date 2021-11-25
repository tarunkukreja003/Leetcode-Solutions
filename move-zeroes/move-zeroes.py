class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # [0,0,0,1] --> in-place n elements, n-1 + n-2 = O(n^2) space = O(1)
        # if store it in another array then time O(n) and space O(n)
        # if we have to do it in-place in O(n) time
        
        # 2 pointer approach - one will be on 0 and the other on the number
        
        # [0,0,0,1,1,1,0]
        
        # to start one pointer will be on first 0 and the other pointer will be on the first non-zero number after first zero
        
        i, j = 0, 0
        
        # first both pointers should point to the first zero
        while i<len(nums) and (nums[i] != 0):
                i += 1
                j += 1
        print(i,j)
        
        while j < len(nums):
            
            # if both are pointing to 0 then which ever is towards the right move it ahead and if both are same then move anyone ahead until the pointer points to non-zero
            
            if (nums[i] == 0 and nums[j] == 0 and j>=i):
                while j < len(nums) and nums[j] == 0:
                    j += 1
            
            elif (nums[i] != 0 and nums[j] == 0):
                while i < len(nums) and nums[i] != 0:
                    i += 1
            
                
            
            # swap elements and increment both pointers, check for both pointers, 0 or non-zero
            elif (nums[i] == 0 and nums[j] != 0 and j>i):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            
            # if both are non-zero
            else:
                i += 1
                j += 1
            
            
                
            
        return nums  
        