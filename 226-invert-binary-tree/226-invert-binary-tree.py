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
        """
        
        """
        invert means swapping the left and right child of every node
        
        """
        
        def swapChild(currNode):
            if currNode is None:
                return
            elif not currNode.left and not currNode.right:
                # there is nothing to swap
                return currNode
            elif currNode.left and not currNode.right:
                currNode.right = currNode.left
                currNode.left = None
                swapChild(currNode.right)
            elif currNode.right and not currNode.left:
                currNode.left = currNode.right
                currNode.right = None
                swapChild(currNode.left)
                
            elif currNode.left and currNode.right:
                # swap them
                currNode.left, currNode.right = currNode.right, currNode.left
                swapChild(currNode.left)
                swapChild(currNode.right)
        
        swapChild(root)
        return root
                
        