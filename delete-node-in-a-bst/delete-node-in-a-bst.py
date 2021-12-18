# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def successor(self, root):
        """
        One step right and then always left
        """
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def predecessor(self, root):
        """
        One step left and then always right
        """
        root = root.left
        while root.right:
            root = root.right
        return root.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # first we have to search the node
        # if the nodeToDelete doesn't have any child then just delete it
        # if the node has a left child - then we'll replace the node by its predeccer which will be the rightmost element of the node's left child. after you have replaced then delete the leaf which was the predecessor
        # if the node has a right child - then we'll replace the node by its successor which will be the leftmost node of the node's right child. after you have replaced then delete the leaf which was the successor

        if not root:
            return None
        
        if root.val > key:
            root.left = self.deleteNode(root.left, key)

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        else:
            # node found

            if not (root.left or root.right):
                root = None

            elif root.left:
                # find predecessor and replace
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)

            else:
                # find successor and replace
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)


        
        return root
                                    
                
                
            
        
        
        
        
        