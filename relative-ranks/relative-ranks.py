import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # score = [3,9,2,1,6]
        # athlete 0 has score 3
        # athlete 1 has score 9
        # sorting and hashmap -> first solution -> O(n) time complexity and O(n) space complexity
        
        # answer = [0] * n
        
        
        # another solution is heap
        # building the heap -> O(n) time, making the answer array -> O(nlogn) because for every item of answer we have to heappop and maintain the heap property, so for every append to answer array we are doing logn work
        
        n = len(score)
        answer = [0] *n
        
        heap = []
        
        for i, score in enumerate(score):
            heapq.heappush(heap,(-score, i))
        
        count = 0
        while heap:
            score, i = heapq.heappop(heap)
            count += 1
            
            if count == 1:
                answer[i] = 'Gold Medal'
            elif count == 2:
                answer[i] = 'Silver Medal'
            elif count == 3:
                answer[i] = 'Bronze Medal'
            else:
                answer[i] = str(count)
        
        return answer
                
        
        