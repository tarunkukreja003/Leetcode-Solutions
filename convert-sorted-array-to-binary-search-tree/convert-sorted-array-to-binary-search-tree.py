# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # [1,2,3,4,5,6,7]
        
        # the current element will be the root, the left of it will be the left subtree and right of it will be the right subtree
        
        def buildBST(arr, low, high):
            if low > high:
                return
            mid = ((high - low) // 2) + low
            
            node = TreeNode(arr[mid])
            node.left = buildBST(arr, low, mid-1)
            node.right = buildBST(arr, mid+1, high)
            
            return node
        
        return buildBST(nums, 0, len(nums)-1)
        
        
            
        