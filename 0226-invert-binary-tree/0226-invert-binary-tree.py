# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        
        swap the children of every node
        """
        
        def invertNode(currNode):
            if currNode is None:
                return 
            currNode.left, currNode.right = currNode.right, currNode.left
            invertNode(currNode.left)
            invertNode(currNode.right)
        
        invertNode(root)
        return root
        