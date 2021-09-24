# https://leetcode.com/problems/house-robber/discuss/156523/From-good-to-great.-How-to-approach-most-of-DP-problems.
class Solution:
    def rob(self, nums: List[int]) -> int:
        ## either we'll rob the current house or will not rob the current house
        ## if we rob the current House i then we'll have all the options from i-2
        ## if we don't rob the current house then we'll have all the options from i-1
        ## we'll do it using memoisation + recursion(top-down)
        memo = [-1] * (len(nums) + 1)
        ## we are keeping the length of memo = len + 1 because the current element i is made of  2 previous elements ---> i-1, i-2 
        if not nums:
            return 0
        def robRecursive(nums, i):
            if i < 0:
                return 0
            if memo[i] >= 0:
                return memo[i]
            
            res = max(robRecursive(nums, i-2) + nums[i], robRecursive(nums, i-1))
            memo[i] = res
            return res
        
        return robRecursive(nums, len(nums)-1)