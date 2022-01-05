# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # we basically have to print the rightmost child of the current level
        # we'll be using queue, just append to the output the last element for the current level
        
        output = []
        if not root:
            return output
        q = collections.deque([(root, 0)])
        
        while q:
            node, level = q.popleft()
            
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))
            
            while q and q[0][1] == level:
                node, level = q.popleft()
                
                if node.left:
                    q.append((node.left, level+1))
                if node.right:
                    q.append((node.right, level+1))
            
            lastElementForCurrentLevel = node.val
            output.append(lastElementForCurrentLevel)
        
        return output
            
            
            
            
                
                
            
        
        
            