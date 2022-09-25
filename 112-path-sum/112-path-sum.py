# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        
        """
        
        can the tree have 0 nodes? Yes, now if the sum required is 0 then will it be true or false? -> false
        can targetSum be -ve? -> yes
        the node values can be -ve -> yes
        
        
        if we reach the leaf and its not eqaul to the path sum then return False to the parent
        
        
        runningSum += currNode.val
        
        if current node is leaf node: 
            if runningSum == targetSum then return True
            else:
                return False
        
        
        for the current node:
        
        if rightTraverse or leftTraverse is True then return True
        else
         return False
         
         
        
        
        """
        
        
        
        def recursivePathSum(currNode, runningSum):
            if not currNode:
                return False
            runningSum += currNode.val
            if not currNode.left and not currNode.right:
                if runningSum == targetSum:
                    return True
                else:
                    return False
            leftSubtreeSum = recursivePathSum(currNode.left, runningSum)
            rightSubtreeSum = recursivePathSum(currNode.right, runningSum)
            
            if leftSubtreeSum or rightSubtreeSum:
                return True
            else:
                return False
        
        return recursivePathSum(root, 0)
        
        