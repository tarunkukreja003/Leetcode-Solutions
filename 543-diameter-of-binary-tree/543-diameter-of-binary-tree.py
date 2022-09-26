# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        """
        
        for the current node the diameter can be either through the curr node or not
        
        if including curr node then depth of left subtree + depth of right subtree + 1
        
        
        the curr node will return the diameter of the curr node and the height to parent
        
        max(diameter of left subtree, diameter of right subtree, depth of right subtree + depth of left subtree + 1)
        
        if we go with top-down approach -> O(n^2) since one node will be visited more than once
        we'll go with bottom-up approach-> why? -> here the time complexity will be O(n) , space complexity will be O(n) because when we're going down the tree then at max there can be n recursion calls
        
        [diameter including the node, height of the tree]
        
        """
        
        def goDownTheTree(currNode):
            if currNode is None:
                return [0, 0]
            # if we have reached the leaf node return 1 which will be covered in the following steps
            leftTreeDiameter, leftTreeHeight = goDownTheTree(currNode.left)
            rightTreeDiameter, rightTreeHeight = goDownTheTree(currNode.right)
            
            
            
            
            diameterOfCurrNode = max(leftTreeDiameter, rightTreeDiameter, leftTreeHeight + rightTreeHeight)
                
            
            heightOfCUrrNode = max(leftTreeHeight, rightTreeHeight) + 1
            
            return (diameterOfCurrNode, heightOfCUrrNode)
        
        return goDownTheTree(root)[0]     
            