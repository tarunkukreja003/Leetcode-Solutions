class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force solution will be O(n^3)
        # a better solution will be the outer loop will have the element and the inner loop will get a target sum of -element -> inner loop is 2 sum which can be done in O(n) time, hence the total complexity of the solution will be O(n^2)
        
        triplets = []
        duplicates = set()
        
        
        
        
        for i, negativeTargetSum in enumerate(nums):
            targetSum = -negativeTargetSum
            twoSumDictionary = {}

            for j in range(i+1, len(nums)):
                # i and j should not be same in triplets
                element = nums[j]
                if element not in twoSumDictionary:
                    twoSumDictionary[targetSum-element] = j
                else:
                    # target sum found
                    # found triplet
                    if i != j:
                        thirdElementIndex = twoSumDictionary[element]
                        triplet = sorted([negativeTargetSum, nums[thirdElementIndex], element])
                        if (triplet[0],triplet[1])  not in duplicates:
                            duplicates.add((triplet[0],triplet[1]))
                            # look for 2 elements same
                            triplets.append(triplet)
                            # if the triplet is already there then don't include that
                        
        return triplets