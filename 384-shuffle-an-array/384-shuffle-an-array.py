from random import randint
class Solution:

    def __init__(self, nums: List[int]):
        self.numsCopy = nums
        self.nums = list(nums)
        
        

    def reset(self) -> List[int]:
        # print(self.numsCopy)
        return self.numsCopy

    def shuffle(self) -> List[int]:
        
        for i in range(len(self.nums)):
            randomIndex = randint(0,len(self.nums)-1)
            self.nums[i], self.nums[randomIndex] = self.nums[randomIndex], self.nums[i] 
        
        return self.nums
            
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()