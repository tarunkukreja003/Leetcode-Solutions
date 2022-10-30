class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        
        
        [1,     1,  1,0 -> 1,0->1,0->1,1,1,1,1,0->1] k = 2
                             L     R
        
        [0, 0, 1]  k=0
        l,r
        
        remainingFlips = 1
        zeroesQueue = [4]
        longestWindowLength = 6
        
        
        
        
        
        """
        left, right = 0,0
        zeroesQueue = deque([])
        remainingFlips = k
        longestLength = 0
        while right < len(nums): 
            currWindowLength = right - left
            while right < len(nums) and nums[right] == 1:
                right += 1
                currWindowLength += 1

            while right < len(nums) and nums[right] == 0 and remainingFlips > 0:  
                remainingFlips -= 1
                zeroesQueue.append(right)
                right += 1
                currWindowLength += 1

            longestLength = max(longestLength, currWindowLength)
            
             
            
            while right < len(nums) and nums[right] == 0 and remainingFlips == 0:
                if zeroesQueue:
                    minZeroIndexFlipped = zeroesQueue.popleft()

                    while left != minZeroIndexFlipped:
                        left += 1

                    remainingFlips += 1
                    left += 1
                else:
                    # if there are 0 flips allowed -> then just calculate the max consecutive1's already there in the arr
                    # move left and right to 1st 1 after the current index
                    while left < right:
                        left += 1
                    
                    while right < len(nums) and nums[right] != 1:
                        left += 1
                        right += 1
                    
                        
                        
                    

        
        return longestLength
        