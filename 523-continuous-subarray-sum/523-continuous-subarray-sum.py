class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        we have to find:
        contiguous subarray of size atleast 2 whose sum is a multiple of k
        
        [24,4,6,7], k = 5
              ^
         
         24/5 = 4.9
         28/5 = 5.6
        the sum has to be divided by k to check if the result is an integer or not, if it is then the sum is a multiple else not
        
        brute-force = start from the first element, and traverse the array and keep on doing the sum until we get sum/k = integer, if we reach the end of the array and didn't get the integer then move to the next element and traverse the rest of the array ahead of it and repeat the process until we get the integer - we will run this until index = n-2[0-based]
        
        time complexity = O(n^2)
        space complexity = O(1)
        
        
        
        
        [23,2,6,4,7], k = 13
         ^
         
        [-21,-8,14,20,25] k =5
         
       
         
        [23,3,6,4,7], k = 13
          ^
          
        
        
        
        [2,4], k = 6
        2%6 = 2
        6%6 = 0, 1
        
        
        [23,2,6,4,7], k = 6
        
        23/6 = float, 23 % 6 = 5
        
        25 % 6 = 1
        
        31 % 6 = 1
        
        the difference btween the indices of mod should be > 1
        
        35 % 6 = 5 this is the answer
        
        2,6,4 is divisible by 6
        
        
        
        
        hashmap = {
         
        }
                  
        
        
        """
        
        currSum = 0
        hashMap = {0:-1}
        
        isContiguousSubArr = False
        
        for i in range(len(nums)):
            currSum += nums[i]
            mod = currSum % k
            
            if mod in hashMap:
                if i-hashMap[mod] > 1:
                    isContiguousSubArr = True
            else:
                hashMap[mod] = i
        
        if isContiguousSubArr:
            return True
        else:
            return False
            
        
        
        