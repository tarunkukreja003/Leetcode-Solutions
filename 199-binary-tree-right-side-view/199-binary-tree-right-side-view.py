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
        
        # time complexity - O(n) , space complexity - queue can have a max of a level's elements and there can be a maximum of N/2 elements in the last level -> O(N)
        
        output = []
        if not root:
            return output
        
        q = collections.deque([(root, 0)])
	
        while q:
            node, level = q.popleft()

            if (q and q[0][1] == level + 1) or not q:
                output.append(node.val)

            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))

        return output