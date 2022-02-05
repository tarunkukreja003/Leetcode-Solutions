class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        """
        
        def findMaximumScore(i, left, right):
            
            if i >= len(multipliers):
                return 
            
            # for multiplier[i] I can choose either from left end or right end
            
            currMult = multiplier[i]
            multiplier[i] = max(findMaximumScore(i+1, left+1, right) + nums[left]*currMult,  findMaximumScore(i+1, left, right - 1) + nums[right]*currMult)
            
        
        
        the problem with keeping more than 2 states in a DP problem is that we'll have to create memoization array having dimensions equal to the states. If there are 2 states then we need a 2d array
        
        left = 0
        
        right = len(nums) - 1 
        
        i = 0
        left = 0
        
        i -> total number of operations performed till ith multiplier
        
        we need the index of right 
        
        left = the total number of left operations performed and the curr Index of left
        right = the total number of right operations performed
        
        left + right = i
        rightOperationsPerformed = i - left
        
        currIndexOfRight = n - 1 - rightOperationsPerformed(i-left)
        
        now if we select right what to pass in the recursion progress? 
        
        in the progress when right is selected we need currIndexOfRight - 1 in the progress and left is left undisturbed. But since we only have 2 progress states left and i, the recursion progress will be (i+1, left) because from the equation above of currIndexOfRight:
        
        currIndexOfRight - 1 = n - 1 - (i+1-left)
        
        
        
        
        findMaximumScore(0, left, right)
        
        """
        
#         n = len(nums)
        
        
#         @lru_cache(2000)
#         def findMaximumScore(i, left):
            
#             if i >= len(multipliers):
#                 return 0
            
#             # for multiplier[i] I can choose either from left end or right end
            
#             currMult = multipliers[i]
#             # rightOperationsPerformed = i-left
#             rightIndex = n - 1 - (i-left)
            
#             leftNumSelected = findMaximumScore(i+1, left+1) + nums[left]*currMult
#             rightNumSelected = findMaximumScore(i+1, left) + nums[rightIndex]*currMult
            
#             return max(leftNumSelected, rightNumSelected)
            
        
        
#         left = 0
        
#         return findMaximumScore(0, left)
    
        
        # bottom - up
        
        # initialise dp with size = [m][m]
        
        m = len(multipliers)
        n = len(nums)
        
        dp = [[ 0 for _ in range(m+1)] for _ in range(m+1)]
        
        # set the base cases and return statement
        
        # since the return val is at 0, 0 the base case would be at the opposite end which is m, m, which is already set to 0
        
        # time for for loops, here there are 2 states, hence we'll have nested loops
        
        
        # we are starting from m-1 even though the dp array has m as the last index, so that i+1 doesn't go out of bounds
        for i in range(m-1,-1,-1):
            # left <= i, left can be max = i when no right operation was selected 
            for left in range(i,-1,-1):
                
                currMult = multipliers[i]
                rightIndex = n - 1 - (i-left)
                
                leftNumSelected = dp[i+1][left+1] + nums[left]*currMult
                rightNumSelected = dp[i+1][left] + nums[rightIndex]*currMult
            
                dp[i][left] = max(leftNumSelected, rightNumSelected)
                
                
                
                
        
        
        
        
        return dp[0][0]
        
        
    
        
        
        