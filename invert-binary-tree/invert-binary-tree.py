import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # bfs
        # is it necessary that a node has both left and right child? - no single child can change postions
        
        if not root:
            return root
        queue = collections.deque([(root)])
        
        while queue:
            currNode = queue.popleft()
            if not currNode.left and not currNode.right:
                continue
            # there is only 1 child
            if not currNode.left and currNode.right:
                currNode.left = currNode.right
                currNode.right = None
                queue.append(currNode.left)
            
            elif not currNode.right and currNode.left:
                currNode.right = currNode.left
                currNode.left = None
                queue.append(currNode.right)
            
            
            # if both the childs are there then swap them
            elif currNode.right and currNode.left:
                currNode.right, currNode.left = currNode.left, currNode.right
                queue.append(currNode.left)
                queue.append(currNode.right)
        
        
        return root
            
            
        
        