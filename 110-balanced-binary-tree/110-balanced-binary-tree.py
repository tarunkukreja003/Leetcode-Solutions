# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        
        if there is no nodes then ? balanced -> true
        if there is 1 node then also -> yes
        
        for every node we'll have to check whether it is balanced or not
        
        space complexity -> 
        time complexity -> 
        
        if there are n nodes in a balanced binary tree, its height is 
        logn -> 1
        
        we stop as soon as we see the tree is not balanced
        
        while checking for every node for balanced subtrees, we'll only reach the leaf node if their parent is balanced tree
        
        in a balanced tree on every level the time complexity for checking balanced tree will be O(n) and then using 1, the total time complexity is n X logn = O(n logn)
        
        
                o    n          
                /\
                o o  (n/2 + n/2)
                   .
                   .                   height = logn
                   .
                   
                   
        
        
        bottom-up approach
        https://www.youtube.com/watch?v=QfJsau0ItOY
        start from the leaf node, check if it is balanced and return [Bool, height] to parent
        
        if Bool is False, keep returning False to curr node's parent
        
        if Bool is True from both the left subtree and right subtree then check their height and return max(leftSubtreeHeight, rightSubtreeHeight) + 1 for the current node and True to its parent
        
        since every node will only be visited only twice, once while going down the tree, and other time while coming up, hence the time complexity = O(n)
        
        space complexity -> if the tree is skewed then the worst case space  will be O(n), else, if it is balanced then O(logn), basically 
        O(h)
        """
        
        # O(n) time complexity -> bottom-up approach
        
        def traverseDownTheTree(node):
            if not node:
                return [True, 0]
            leftSubtree =traverseDownTheTree(node.left)
            rightSubtree = traverseDownTheTree(node.right)
            
            balanced = (leftSubtree[0] and rightSubtree[0] and abs(leftSubtree[1] - rightSubtree[1]) <= 1)
            
            return [balanced, max(leftSubtree[1], rightSubtree[1]) + 1]
        return traverseDownTheTree(root)[0]
            
            
        
#         # O(nlogn) -> top -down approach
#         def findDepth(node):
#             if node is None:
#                 return 0
            
#             leftSubtreeHeight = findDepth(node.left)
#             rightSubtreeHeight = findDepth(node.right)
            
#             return max(leftSubtreeHeight, rightSubtreeHeight) + 1
        
#         def isBalancedBinaryTree(node):
#             if node is None:
#                 return True
#             leftSubtreeHeight = findDepth(node.left)
#             rightSubtreeHeight = findDepth(node.right)
            
#             if (leftSubtreeHeight > rightSubtreeHeight + 1) or (rightSubtreeHeight > leftSubtreeHeight + 1):
#                 return False
#             else:
#                 return (isBalancedBinaryTree(node.left)) and (isBalancedBinaryTree(node.right))
        
#         return isBalancedBinaryTree(root)
            
            
                            
        