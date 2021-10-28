# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # bfs using queue
        
        if not root:
            return 0
        # we'll have to track level
        que = collections.deque([(root,0)])
        
        
        
        while que:
            (parentNode, level) = que.popleft()
            
            if (parentNode.left) or parentNode.right:
                level += 1
            
            if (parentNode.left):
                que.append((parentNode.left, level))
            
            if parentNode.right:
                que.append((parentNode.right, level))
            
        return (level + 1)
                
            