import heapq
import math

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = self.buildGraph(n, edges, succProb) # adjacency list
        # 2 create a maxHeap and iniitalize it with start node
        heap = MaxHeap([(1, start)])
        visited = set()
        probabilities = [0 for _ in range(n)]
        probabilities[start] = 1
        
        # 3. While heap is not empty
            # 3.1 take element from heap: (currProbability, node)
            # 3.2 if element was visited, continue
            # 3.3 if currNode == end: return currProbability
            # 3.4 traverse neighbors
                # 3.4.1 if probability to neighbor > probabilities[neighbor] and neighbor not in visited
                    # 3.4.1.1 probabilities[neighbor] = new probality
                    # 3.4.1.2 add neighbor to heap: heap.push((cost, node))
                    
        while not heap.isEmpty():
            (currProbability, currNode) = heap.pop()
            if currNode in visited: continue
            visited.add(currNode)
            
            for (neighborProbability, neighbor) in graph[currNode]:
                newProbability = currProbability * neighborProbability
                if newProbability > probabilities[neighbor] and neighbor not in visited:
                    probabilities[neighbor] = newProbability
                    heap.push((newProbability, neighbor))
        
        return probabilities[end]
    
    def buildGraph(self, vertices, edges, costs):
        graph = [[] for i in range(vertices)]
        
        for i, (nodeA, nodeB) in enumerate(edges):
            cost = costs[i]
            graph[nodeA].append((cost, nodeB))
            graph[nodeB].append((cost, nodeA))
        
        return graph

    
class MaxHeap:
    def __init__(self, arr = []):
        self.heap = [(-cost, node) for (cost, node) in arr]
        heapify(self.heap)
        
    def peek(self):
        return self.heap[0]
    
    def pop(self):
        cost, node = heappop(self.heap)
        return (-cost, node)
    
    def push(self, value):
        cost, node = value
        heappush(self.heap, (-cost, node))
    
    def isEmpty(self):
        return len(self.heap) == 0
    