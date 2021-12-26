# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        # do inorder traversal of the BST and put it in an array
        # this array is almost sorted with just two elements swapped, find them and swap them, then make BST
        
        almostSortedArr = []
        
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            almostSortedArr.append(node.val)
            inorder(node.right)
        
        
        
        # print(almostSortedArr)
        
        # write a function to swap 2 nodes in an almost sorted array
        
        def findTwoSwappedNodes(arr):
            i, j = 0,0

            while i< len(arr)-1:
                if arr[i+1] < arr[i]:
                    # ith element is the first
                    j = i+1
                    while j < len(arr)-1:
                        if arr[j+1] < arr[j]:
                            # j+1 is the second element
                            # swap i and j+1
                            return (arr[i], arr[j+1])
                        j += 1

                    # if we didn't find the second element till after reaching the end of arr, then swap i+1 and i
                    return(arr[i], arr[i+1])

                i += 1

        
        
        
        
        def recover(node, x, y, count):
            if node:
                if node.val == x or node.val == y:
                    node.val = y if node.val == x else x
                    count -= 1
                    
                    if count == 0:
                        return
                
                recover(node.left, x, y, count)
                recover(node.right, x, y, count)
        
        inorder(root)
        x,y = findTwoSwappedNodes(almostSortedArr)
        recover(root,x,y,2)
        
        return root
        