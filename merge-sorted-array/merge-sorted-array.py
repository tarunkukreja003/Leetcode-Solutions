class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        i, j, k = 0, 0, 0
        
        mergedSortedArr = []
        
        while (i<m) and (j < n):
            if nums1[i] >= nums2[j]:
                # print("if statement i === ", i)
                mergedSortedArr.append(nums2[j])
                j += 1
                k += 1
                
            elif nums1[i] < nums2[j]:
                print("elif statement i === ", i)
                mergedSortedArr.append(nums1[i])
                i += 1
                k += 1
        
        ## if elements are left
        while i<m:
            mergedSortedArr.append(nums1[i])
            i += 1
            k += 1
        
        while j<n:
            mergedSortedArr.append(nums2[j])
            j += 1
            k += 1 
            
            
            
        for z in range(len(nums1)):
            nums1[z] = mergedSortedArr[z]
        
        
        
                
                
        