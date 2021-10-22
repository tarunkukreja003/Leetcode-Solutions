class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factorsList = []
        
        for i in range(1, n+1):
            if (n%i) == 0:
                factorsList.append(i)
        
        if len(factorsList) < k:
            return -1
        
        return factorsList[k-1]
        