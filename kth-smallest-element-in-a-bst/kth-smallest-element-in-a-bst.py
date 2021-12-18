# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # for smaller values I'll go to the left, I'll maintain a stack and keep pushing while traversing to leftmost element
        # then we'll consider k
        # if the top of the stack doesn't have any right child then just pop it
        # if the top of the stack has a right child then pop it and traverse the left in order of the right child of the node
        # in every pop decrease k by 1 and continue until k = 0
        
        
        
        # [3]
        # kthSmallestValue = 1
        
        inorderLeftStack = []
        kthSmallestValue = None
        
        def leftSubtreeTraversal(node):
            if node == None:
                return
            inorderLeftStack.append(node)
            leftSubtreeTraversal(node.left)
        
        leftSubtreeTraversal(root)
        
        while k > 0:
            stackTopNode = inorderLeftStack.pop()
            
            if stackTopNode.right:
                leftSubtreeTraversal(stackTopNode.right)
            
            
            k -= 1
            kthSmallestValue = stackTopNode.val
        
        return kthSmallestValue
        
        
        