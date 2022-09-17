# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        """
        inorder traversal -> left, key, right
        
        
        """
        
        self.inorderTraversalList = []
        
        def inorderBinaryTreeTraversal(node):
            if node is None:
                return 
            inorderBinaryTreeTraversal(node.left)
            self.inorderTraversalList.append(node.val)
            inorderBinaryTreeTraversal(node.right)
    
        inorderBinaryTreeTraversal(root)
        
        return self.inorderTraversalList