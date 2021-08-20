# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        outputArr = []
        
        def recursiveInorder(rootNode):
            if rootNode == None:
                return
            recursiveInorder(rootNode.left)
            outputArr.append(rootNode.val)
            recursiveInorder(rootNode.right)
        
        recursiveInorder(root)
        return outputArr
            
        