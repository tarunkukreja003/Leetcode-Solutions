class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        [3,4,2,5] target = 7 -> here 7 has 2 solutions -> such case doesn't exist
        can there be multiple solutions possible? no
        
        [3,3,2,5] target = 6 -> can there be duplicates and can they add upto the target? -> yes
        [3,4,3] target = 7 -> this case is invalid -> 2 solutions exists
        
        if none add upto the sum then? there is actually a solution in every test case
        
        ----------------
        brute-force
        
        [4,3,3,2] target = 6
             ^
        for every element sum it with the elements ahead of it in the array. If the sum == target then break
        
        time complexity -> O(n^2)
        space complexity -> O(1)
        
        --------------------
        can we optimize it using some extra space?
        can we do it in 1 pass?
        [4,3,3,2] target = 6
        
        6-4 = 2
        6-3 = 3
        6-3 = 3
        
        [2,5,3] target = 7
        
        7-2 = 5
        7-5 = 2
        
        {
        5:0
        
        }
        
        if we make a hashmap which contains target-element as its key and the value will be the index of the element
        
        while traversing the loop we'll check whether the current element is there in the hashmap or not, if it is , then ans is [index-value, index-of-current-element]
        if it is not then store target - current element and its index in the hashmap
        
        element1 + element2 = target
        element2 = target - element1
        
        """
        
        diffToIndexMapping = {}
        
        for i, element in enumerate(nums):
            if element not in diffToIndexMapping:
                difference = target - element
                diffToIndexMapping[difference] = i
            else:
                index1 = diffToIndexMapping[element]
                return [index1, i]
                
                
        