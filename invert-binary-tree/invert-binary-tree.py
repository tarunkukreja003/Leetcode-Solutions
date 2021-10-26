# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # iterative solution
        
        # [7,2] 
        # 
        nodeQueue = [root]
        currentNode = root
        
        while True:
            if currentNode != None:
                currentNode.left, currentNode.right = currentNode.right, currentNode.left
                
                if currentNode.left != None:
                    print(currentNode.left.val)
                    nodeQueue.append(currentNode.left)
                
                if currentNode.right != None:   
                    print(currentNode.right.val)
                    nodeQueue.append(currentNode.right)
                
                nodeQueue = nodeQueue[1:]
                if nodeQueue:
                    parentNode = nodeQueue[0]
                    currentNode = parentNode
                else:
                    currentNode = None
                
                
                
            
            elif len(nodeQueue) == 0:
                break;
            
            else:
                break;
        
        return root
                
            
            
        
        
            
            
        