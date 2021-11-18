class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## if the array is sorted in descending order then 0
        ## [(1,4), (3,2), (6,4), (7,1), (8,5), (11,3)] --> sorting won't help
        
        ## O(n^2) brute force is checking every element with every other element infront of it
        ## We have to find the maximum difference but maxDiff = x[j] - x[i] where j > i
        
        ## We have to do it in O(n) time
        ## We can keep track of minPrice and the maxProfit
        
        minPrice = float('inf')
        maxProfit = 0
        
        for i in range(len(prices)):
            if minPrice > prices[i]:
                minPrice = prices[i]
            elif (prices[i] - minPrice) > maxProfit:
                maxProfit = prices[i] - minPrice
        
        return maxProfit
        
        