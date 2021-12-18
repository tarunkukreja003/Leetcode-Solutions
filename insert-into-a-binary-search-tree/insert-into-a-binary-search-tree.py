# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # if currNode val is greater than the insertion value then traverse left else traverse right
        # when we reach the leaf insert to the left or right of it which depends whether it is greater or less than the leaf node
        
        
        def insertNodeIntoBST(node, nodeToBeInserted):
            if not node:
                return
            
            
            # if the currNode only has 1 node or even if its the leaf node
            if node.val > nodeToBeInserted.val and not node.left:
                node.left = nodeToBeInserted
            elif node.val < nodeToBeInserted.val and not node.right:
                node.right = nodeToBeInserted
                
            
            if node.val > nodeToBeInserted.val:
                return insertNodeIntoBST(node.left, nodeToBeInserted)
            
            elif node.val < nodeToBeInserted.val:
                return insertNodeIntoBST(node.right, nodeToBeInserted)
            
        nodeToBeInserted = TreeNode(val)
        if not root:
            root = nodeToBeInserted
        insertNodeIntoBST(root, nodeToBeInserted)   
        
        return root
                    
                
            
            
                
            
            
                
                
        
        
        