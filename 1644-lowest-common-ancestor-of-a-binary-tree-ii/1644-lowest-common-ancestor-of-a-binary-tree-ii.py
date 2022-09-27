# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        """
        are all nodes unique in the tree?->yes
        if both of them exist then are they both different from each other? -> yes -> p != q
        
        the only case where the code of LCA 1 will break is:
        
        if we find both p and q in the tree then only the algorithm for LCA 1 will work else return null
        
        Tree:
        
        p
        
        or 
        
        q
        
        """
        
        def dfsFindP(currNode):
            if currNode is None:
                return False
            
            if currNode.val == p.val:
                return True
            
            return dfsFindP(currNode.left) or dfsFindP(currNode.right)
        
        def dfsFindQ(currNode):
            if currNode is None:
                return False
            
            if currNode.val == q.val:
                return True
            
            return dfsFindQ(currNode.left) or dfsFindQ(currNode.right)
        
        if dfsFindP(root) and dfsFindQ(root):
            # write the code for finding LCA
            
            def findLCA(currNode):
                # [currLowestAncestor, Bool->whether p or q found or not in the currNode tree]
                
                if currNode is None:
                    return [None, False]
                
                if currNode.val == p.val or currNode.val == q.val:
                    return [currNode, True]
                leftLowestAncestor, leftBoolVal = findLCA(currNode.left)
                righLowestAncestor, rightBoolVal = findLCA(currNode.right)
                
                
                if leftBoolVal and rightBoolVal:
                    return [currNode, True]
                elif not leftBoolVal and rightBoolVal:
                    return [righLowestAncestor,True]
                elif not rightBoolVal and leftBoolVal:
                    return [leftLowestAncestor, True]
                else:
                    return [None, False]
                
            return findLCA(root)[0]
                
        else:
            return False
            
        