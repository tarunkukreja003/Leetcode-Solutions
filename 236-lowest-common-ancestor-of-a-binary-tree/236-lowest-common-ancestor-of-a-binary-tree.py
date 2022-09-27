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
        are all the nodes unique in the tree? yes
        even if all nodes are not unique but p and q are unique -> then also it will work
        
        is p and q unique? yes
        p!=q
        
        is it possible that the tree is empty? 0 nodes? ->no
        1 node? -> no minimum of 2 nodes
        
        will p and q always exist in the tree? -> yes
        
        
        -------------------------------------
        .
        .
        .
        p
         \
          q
         LCA= p
        
        first we'll find p or q whichever we find first using DFS
        

        
        """
        
        def dfsLCA(currNode):
            if currNode is None:
                return [None, False]
            if currNode.val == p.val:
                return [p, True]
            if currNode.val == q.val:
                return [q, True]

            lcaInLeft, leftBoolVal= dfsLCA(currNode.left)
            lcaInRight, rightBoolVal = dfsLCA(currNode.right)



            if leftBoolVal and rightBoolVal:
                # currNode is the LCA
                return [currNode, True]
            elif not leftBoolVal and rightBoolVal:
                # lca in right
                return [lcaInRight, True]
            elif not rightBoolVal and leftBoolVal:
                return [lcaInLeft, True]
            else:
                return [None, False]
        
        return dfsLCA(root)[0]