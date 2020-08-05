# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructBSTfromSortedArray(self, low, high):
        if low > high:
            return
        mid = low + (high - low) // 2
        
        rootNode = TreeNode(self.sortedArray[mid])
        rootNode.left = self.constructBSTfromSortedArray(low, mid-1)
        rootNode.right = self.constructBSTfromSortedArray(mid+1, high)
        
        return rootNode
    def sortedArrayToBST(self, nums):
        self.sortedArray = nums
        return self.constructBSTfromSortedArray(0, len(nums)-1)
        

