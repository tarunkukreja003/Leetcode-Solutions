class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumNums = 0
        totalSumRequired = 0
        
        for num in nums:
            sumNums += num
        
        for i in range(len(nums)+1):
            totalSumRequired += i
        
        return totalSumRequired - sumNums
        
        