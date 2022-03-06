# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        # first let's find the start node
        def searchStartNode(startNodeVal, node):
            if node == None:
                return
            if startNodeVal == node.val:
                return node
            return searchStartNode(startNodeVal, node.left) or searchStartNode(startNodeVal, node.right)
        
        startNode = searchStartNode(startValue, root)
        
        # assign parent to every node
        def assignParent(node, parent=None):
            if node:
                node.parent = parent
                assignParent(node.left, node)
                assignParent(node.right, node)

        assignParent(root)
        
        
        # now, from the start node we can go either left, right or to the parent to search for destination
        
        # going left and right from the start node
        directionStack = []
        def traverseChildNodesOfStartNode(destValue, node):
            if node is None:
                return False
            if node.val == destValue:
                return True
            
            # traversing left
            directionStack.append('L')
            if traverseChildNodesOfStartNode(destValue, node.left):
                return True
            else:
                directionStack.pop()
                
            # traversing right
            directionStack.append('R')
            if traverseChildNodesOfStartNode(destValue, node.right):
                return True
            else:
                directionStack.pop()
            
        
        def traverseParentOfStartNode(destValue, node):
            if node is None:
                return False
            
            parent = node.parent
            
            if parent is None:
                return False
            
            if parent.val == destValue:
                return True
            # we'll check whether the node is left or right of the parent and traverse the other child to find dest node
            
            if parent.left == node:
                # travserse right child to find the dest value
                directionStack.append('R')
                if traverseChildNodesOfStartNode(destValue, parent.right):
                    return True
                else:
                    directionStack.pop()
                    
            elif parent.right == node:
                # travserse right child to find the dest value
                directionStack.append('L')
                if traverseChildNodesOfStartNode(destValue, parent.left):
                    return True
                else:
                    directionStack.pop()
            
            directionStack.append('U')
            if traverseParentOfStartNode(destValue, parent):
                return True
            else:
                directionStack.pop()
                
            
            
                    
                    
            
        
        pathString = ""
        
        if traverseChildNodesOfStartNode(destValue, startNode):
            ## the path is direction stack
            for direction in directionStack:
                pathString += direction
        else:
            # the path lies in the parent of startNode
            directionStack.append('U')
            if traverseParentOfStartNode(destValue, startNode):
                for direction in directionStack:
                    pathString += direction
            else:
                directionStack.pop()
        
        return pathString
        
            
        
        
        