class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # [-3,10,-3] k = 7 ans = 2
        # [-3,10,-4,11] k =7 ans = 2
        # [-9,-10] k = -19 ans = 1
        # [-9,0]  k = 8 ans = 0
        
        # [-3,10,-13,-4,11,7] k = 7 ans = 3
        
        # [-3,10,-3] k = 7
        
        # [1,-1,1,1,1] k = 2
        
          # brute-force -> for every element i go from i+1 till end and do leftSum = leftSum - currElement until leftSum == 0 
            # time complexity = O(n^2) and space complexity = O(1)
        """
            currSum = 2
            res = 2
            sumToRemove = currSum - k = 0 this much sum I have to remove from my curr SubArray and this sum should be a part of curr SubArray 
            prefixSums = {
                0:2,
                1:2
                2:1
                
                
            
            
            
            }
            
        
        """
        numberOfContiguousSubArray = 0
        runningSum = 0
        sumToRemoveFreqDict = {0:1}
        
        for n in nums:
            runningSum += n
            sumToRemove = runningSum - k
            
            if sumToRemove in sumToRemoveFreqDict:
                numberOfContiguousSubArray += sumToRemoveFreqDict[sumToRemove]
            
            if runningSum in sumToRemoveFreqDict:
                sumToRemoveFreqDict[runningSum] += 1
            else:
                sumToRemoveFreqDict[runningSum] = 1
                
        return numberOfContiguousSubArray
            
            
                
            
            
            
            
                
        