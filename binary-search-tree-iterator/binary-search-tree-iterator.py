# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.sortedArr = [-1]
        self.inorder(root)
        self.pointer = 0
        
    def inorder(self, node):
        if node == None:
            return
        self.inorder(node.left)
        self.sortedArr.append(node.val)
        self.inorder(node.right)
    
    def next(self) -> int:
        self.pointer += 1
        if self.pointer < len(self.sortedArr):
            return self.sortedArr[self.pointer]
        
        
        

    def hasNext(self) -> bool:
        if (self.pointer+1) < len(self.sortedArr):
            return True
        else:
            return False
        
        
        
        
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

# we'll start from the leftmost node -> the smallest node in the whole tree
