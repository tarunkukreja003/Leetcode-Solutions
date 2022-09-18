# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    from collections import deque
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        """
        
        leftNode.right == rightNode.left
        
        we can do it in BFS
        
        on the current level,if there are odd number of elements, then return False straight away 
        if there are even number of elments then start two pointers from mid and mid+1
        if arr[i] == arr[j]:
            i --
            j ++
        
        else:
            return False
            
        [3,4,4,3]
         i     j
         
         time complexity:
         at every level we are traversing the number of elements on that level
         
         so total elements in all levels = total number of nodes in the tree
         hence time complexity = O(n)

        space complexity = O(n) -> on 1 level there can be n nodes(eg. 1 node only in the tree)
        
        """
        
        
        queue = deque([root, root])
        
        while queue:
            node1 = queue.popleft()
            node2 = queue.popleft()
            
            if not node1 and not node2:
                continue
                
            elif not node1 or not node2:
                return False
            
            if node1.val != node2.val:
                return False
            queue.append(node1.left)
            queue.append(node2.right)
            queue.append(node1.right)
            queue.append(node2.left)
            
        return True
            
                
            
        
        