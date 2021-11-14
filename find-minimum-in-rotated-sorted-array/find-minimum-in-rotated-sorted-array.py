class Solution:
    
            
        
        
    def findMin(self, nums: List[int]) -> int:
        
        def findMinBinarySearch(low, high, arr):
        # if it is the same as original array then the minimum element will be the first element
        
        # [3,4,5,1,2]
        # [4,5,6,7,8,9,10,1,2]
        # if mid - 1 > mid and mid + 1 > mid then return mid
        # we know that there will be smaller elements towards the end of the array, hence we have to move towards them
        # if the array is not rotated then the smaller elements will be at the beginning
        
        
            if low >= high:
                return arr[low]

            mid = ((high - low) // 2) + low

            if (arr[mid - 1] > arr[mid]) and (arr[mid] < arr[mid + 1]):
                return arr[mid]

            if arr[mid] > arr[high]:
                # move towards right
                print("moving towards right current mid element = ", arr[mid])
                return findMinBinarySearch(mid+1, high, arr)
            else:
                # move towards left
                return findMinBinarySearch(low, mid-1, arr)
            
        
        return findMinBinarySearch(0, len(nums)-1, nums)
        
        
        
        