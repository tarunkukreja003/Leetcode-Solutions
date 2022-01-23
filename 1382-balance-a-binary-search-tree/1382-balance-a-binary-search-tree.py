# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""

# for the current Node the height of the left subtree and the right subtree should not differ by more than 1 
    # if the tree is already balanced then we don't need to balance it
    
    # do inorder travseral of BST and store it in an array -> this array will be sorted.
    # now just convert this sorted array to BST, we just have to follow the approach of binary search
    
    
    # doing it in O(1) space is pretty complicated and requires rotations
    # https://leetcode.com/problems/balance-a-binary-search-tree/discuss/541785/C%2B%2BJava-with-picture-DSW-O(n)orO(1)
    
"""
       
class Solution:
    def inorderTraversal(self, root, sortedArray):
        if root == None:
            return 
        self.inorderTraversal(root.left, self.sortedArray)
        self.sortedArray.append(root.val)
        self.inorderTraversal(root.right, self.sortedArray)
        
    def constructBalancedBST(self, low, high):
        if low > high:
            return
        mid = low + (high - low) // 2
        
        rootNode = TreeNode(self.sortedArray[mid])
        rootNode.left = self.constructBalancedBST(low, mid-1)
        rootNode.right = self.constructBalancedBST(mid+1, high)
        
        return rootNode
        
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.sortedArray = []
        self.inorderTraversal(root, self.sortedArray)
        return self.constructBalancedBST(0,len(self.sortedArray)-1)
        