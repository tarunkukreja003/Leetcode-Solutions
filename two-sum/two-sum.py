class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#         # {
#         7: target - curr element: = (2, 0)
        
#         }
#         #
        
#         ##
#         #
        
        sumDict = {}
        
        for (index, num) in enumerate(nums):
            if num in sumDict:
                return [index, sumDict[num][1]]
            else:
                sumDict[target - num] = (num, index)
        
        