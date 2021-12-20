import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # stones
        # heap
        
        # time complexity -> O(nlogn) space complexity -> O(n) store n/2 elements at max
        
        heap = []
        
        # heap q always maintains min heap by default, so we'll be pushing -stoneWeight
        for i, stoneWeight in enumerate(stones):
            heapq.heappush(heap, -stoneWeight)
        print(heap)
        while len(heap)>1:
            stoneWeightHeaviest = heapq.heappop(heap)
            
            stoneWeightSecondHeaviest = heapq.heappop(heap)
            
            stoneWeightHeaviest = -stoneWeightHeaviest
            stoneWeightSecondHeaviest = -stoneWeightSecondHeaviest
            
            
            
            if stoneWeightHeaviest > stoneWeightSecondHeaviest:
                stoneWeightHeaviest = stoneWeightHeaviest - stoneWeightSecondHeaviest
                heapq.heappush(heap, -stoneWeightHeaviest)
            
            
        # print(visited)
        if heap:
            return -heap[-1]
        else:
            return 0
        
        
        
        
        
        
        
        