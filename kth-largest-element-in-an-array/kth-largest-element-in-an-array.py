from heapq import heappop, heappush, heapify
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []
        heapify(heap)
        for num in nums:
            heappush(heap, -num)
        
        kthLargestElement = float('-inf')
        while k > 0:
            maxElement = heappop(heap)
            kthLargestElement = - maxElement
            k -= 1
        
        return kthLargestElement