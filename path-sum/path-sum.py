# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        # we will have to traverse every path from root to leaf and find if there is the sum
        # if we reach the leaf node and we see that we haven't reached the targetSum we will return and subtract that element from the targetSum
        self.runningSum = 0
        def recursiveRunningSum(root, targetSum):
            if root == None:
                return 
            
            # if we are on a node in the path just add that to the sum
            
            self.runningSum += root.val
            
            # if we reached the leaf node and running sum is not equal to targetSum return and subtract from running sum
            if (root.left) == None and (root.right == None):
                if self.runningSum != targetSum:
                    self.runningSum -= root.val
                    return
                
                elif self.runningSum == targetSum:
                    return True
            
            
            leftResult = recursiveRunningSum(root.left, targetSum)
            rightResult = recursiveRunningSum(root.right, targetSum)
            
            if leftResult or rightResult:
                return True
            else:
                self.runningSum -= root.val
                return
            
            
        return recursiveRunningSum(root, targetSum)
            
            
        