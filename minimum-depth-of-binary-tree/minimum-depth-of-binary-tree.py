# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        que = collections.deque([(root, 1)])
        
        while que:
            parentNode, level = que.popleft()
            
            
            if (parentNode.left is None) and (parentNode.right is None):
            # this is the leaf node
                return level
            
            if (parentNode.left is not None):
                que.append((parentNode.left, level + 1))
            
            if (parentNode.right is not None):
                que.append((parentNode.right, level + 1))
            
            
            
            
            
        
        
        
        