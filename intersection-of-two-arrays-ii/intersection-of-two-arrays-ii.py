class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        freqDict = collections.Counter(nums1)
        
        output = []
        for num in nums2:
            if (num in freqDict) and (freqDict[num] >= 1):
                output.append(num)
                freqDict[num] -= 1
                
        return output
        