class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        """
        [1,2,3,1] k = 3
        
        the length of the window is k+1
        
        brute-force
        start with i = 0 to n-k-1-> outer loop
            inner loop -> j=i+1 to i+k+1
                if arr[i] == arr[j]:
                    return True
        
        return False
        
        time complexity -> O(nk)
        
        
        optimal solution:
        
        have a hashmap of num:index
        
        we'll have a sliding window of length = k+1
        
        we'll start at index 0, for the first window elements from 0 to k will be put in the hashmap with their values being their indices
        
        only for first window we'll check for every iteration if the currNum is in hashmap or not, if it there return True else add it to hashmap and slide the window to right
        
        from the second window we'll remove the first element of prev window from hashmap and check if the last element of the 
        currWindow is in hashmap, if it is then return True else slide the window
        
        """
        
        self.numsToIndexHashMap = {}
        # we have to make a window of length k+1
        
        n = len(nums)
        if k > n:
            k = n
            
        firstWindow = nums[:k+1]
        
        for j in range(len(firstWindow)):
            if firstWindow[j] in self.numsToIndexHashMap:
                return True
            else:
                self.numsToIndexHashMap[firstWindow[j]] = j
            
        for i in range(n-k):
            # remove the first element
            
            del self.numsToIndexHashMap[nums[i]]
            
            if i+k+1 < n:
                if nums[i+k+1] in self.numsToIndexHashMap:
                    return True
                else:
                    self.numsToIndexHashMap[nums[i+k+1]] = i+k+1
        
        return False
        
        
        
        