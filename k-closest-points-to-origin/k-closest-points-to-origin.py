from heapq import heappop, heappush, heapify
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # min heap according to distance from origin
        
        heap = []
        heapify(heap)
        for coordinate in points:
            distance = math.sqrt(coordinate[0]**2 + coordinate[1]**2)
            heappush(heap, (distance, coordinate))
        
        kClosestPoints = []
        while k >0:
            (distance, coordinate) = heappop(heap)
            kClosestPoints.append(coordinate)
            k -= 1
        
        return kClosestPoints
        