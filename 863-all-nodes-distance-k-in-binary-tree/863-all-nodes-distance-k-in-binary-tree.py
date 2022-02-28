# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        
        can their be duplicate target values? -> no they are unique
        
        since it si distance it has to be done with DFS
        
        k = 2
        
        find the target node first
        once we found it find the nodes at distance k from it which are its children
        
        
        first annotate the information of parent for every node
        
        let's say we have the information of the parent
        
        once we found the target node we'll start calculating the height upwards
        
        parent at height 1, we'll go down the other child and check for nodes of height == k and also we'll move up the parent(towards ancestors) to check nodes at distance == k
        
        ancestor will be assigned height=child containing target node height + 1
        
        
        time complexity -> 
        
        assigning the parent -> O(n)
        
        visiting every node at most once hence O(n)
        
        space complexity -> worst case recursion stack -> O(n)
        
        
        """
        
        # find the target node
        
        nodesAtDistanceKFromTarget = []
        
        def assignParent(node, parent=None):
            if node:
                node.parent = parent
                assignParent(node.left, node)
                assignParent(node.right, node)

        assignParent(root)
        
        # def traverseTree(node):
        #     if node:
        #         print(node.parent)
        #         traverseTree(node.left)
        #         traverseTree(node.right)
        # print(traverseTree(root))

        # find the child nodes of target at a distance K from target
        def childNodesAtDistanceKFromTarget(node, currHeight):
            if node is None:
                return
            if currHeight == k:
                nodesAtDistanceKFromTarget.append(node.val)
            
            childNodesAtDistanceKFromTarget(node.left, currHeight + 1)
            childNodesAtDistanceKFromTarget(node.right, currHeight + 1)
        
        childNodesAtDistanceKFromTarget(target, 0)
        
        
        ## now parent comes into play
        
        # heightOfParentOfTarget = 1
        
        def findNodesNotChildOfTarget(node, distance):
        # parent will be at height currHeight+1
        # if the currHeight came from left child then only traverse right child and vica versa
            
            if node is None:
                return 
            parentNode = node.parent
            if parentNode is None:
                return
            distanceOfParentNode = distance+1
            if distanceOfParentNode == k:
                nodesAtDistanceKFromTarget.append(parentNode.val)


            if parentNode.left == node:
                # only traverse the right child of the parent node
                childNodesAtDistanceKFromTarget(parentNode.right, distanceOfParentNode+1)

            elif parentNode.right == node:
                childNodesAtDistanceKFromTarget(parentNode.left, distanceOfParentNode+1)
            
            
            findNodesNotChildOfTarget(parentNode, distanceOfParentNode)
        
        
        findNodesNotChildOfTarget(target, 0)
        
        return nodesAtDistanceKFromTarget
        
        
        
        
        