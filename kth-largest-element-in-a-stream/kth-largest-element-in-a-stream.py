import heapq
from heapq import heappop, heappush, heapify
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # the trick to find the kth largest element is actually to use min heap and not max heap
        # in max heap first we'll pop k elements then append k elements - this is not a good approach
        
        # in min heap you just have to keep k elements in the heap -> after this the extractMin will give us the kth largest element
        
        self.k = k
        self.nums = nums
        heapify(self.nums)
        
        while len(self.nums) > self.k:
            heappop(self.nums)

    def add(self, val: int) -> int:
        
        heappush(self.nums, val)
        if len(self.nums) > self.k:
            heappop(self.nums)
        return self.nums[0]
            
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)