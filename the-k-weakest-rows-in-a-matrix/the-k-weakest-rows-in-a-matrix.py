from heapq import heapify, heappop, heappush

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # sort according to the number of -> time complexity = for n rows -> nlogn
        # space complexity -> n because we are storing the tuple of number of soldiers in row i and index of i 
        
        # min heap
        
        # when we do extract min element and we then we do getMin -> we compare whether they are equal or not, if they are then we check their indices, if the index of getMin is less than the popped element then we do another extarctMin and we place the index of recent pop before the one popped
        
        # or maintain min heap according to two parameters -> first priority is number of soldiers and the second is the index if the number of soldiers in a row is same
        
        heap = []
        
        heapify(heap)
        
        for i in range(len(mat)):
            soldierCount = 0
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    soldierCount += 1
            heappush(heap, (soldierCount, i))
        
        
        
        
        kWeakestRowsIndices = []
        
        while k > 0:
            numberOfSoldiers, index = heappop(heap)
            kWeakestRowsIndices.append(index)
            k -= 1
        
        return kWeakestRowsIndices
            
            
                
        