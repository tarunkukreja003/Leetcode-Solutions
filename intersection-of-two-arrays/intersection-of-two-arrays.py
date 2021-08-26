class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        uniqueIntegerDict = {}
        outputArray = []
        
        for num in nums1:
            if num not in uniqueIntegerDict:
                uniqueIntegerDict[num] = False
        
        for num in nums2:
            if (num in uniqueIntegerDict) and (uniqueIntegerDict[num] == False):
                outputArray.append(num)
                uniqueIntegerDict[num] = True
        
        return outputArray
                
                
        