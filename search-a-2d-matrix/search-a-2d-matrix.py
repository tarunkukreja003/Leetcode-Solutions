class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # we will have binary search since if we convert the 2d array into 1d it will be a sorted array 
        
        sortedArr = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                sortedArr.append(matrix[i][j])
        
        print(sortedArr)
        
        def binarySearch(arr, low, high, elementToBeFound):
            
            if low > high:
                return False
            
            mid = low + (high-low)//2
            
            if elementToBeFound == arr[mid]:
                return True
            
            elif elementToBeFound > arr[mid]:
                return binarySearch(arr, mid + 1, high, elementToBeFound)
            else:
                return binarySearch(arr, low, mid - 1, elementToBeFound)
        
        return binarySearch(sortedArr, 0, len(sortedArr) - 1, target)
                
            
            
        