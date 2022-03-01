# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.totalSum = 0
        def findRootToLeafNumbersSum(node, currNumber):
            if node is None:
                return
            currNumber =  currNumber * 10 + node.val
            if node.left is None and node.right is None:
                # this is the leaf node
                self.totalSum += currNumber
            findRootToLeafNumbersSum(node.left, currNumber)
            findRootToLeafNumbersSum(node.right, currNumber)
            
        if root.val is None:
            return 0
        else:
            findRootToLeafNumbersSum(root,0)
        
        return self.totalSum


