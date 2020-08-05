# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getPreOrderArrIndex(self):
        return self.preOrderArrIndex
    def incrementPreOrderArrIndex(self):
        self.preOrderArrIndex += 1
    def constructBst(self, preorderArr, rootVal, minVal, maxVal, sizeOfArr):
        if self.getPreOrderArrIndex() >= self.sizeOfArr:
            return None
        rootNode = None
        
        if (rootVal > minVal) and (rootVal < maxVal):
            rootNode = TreeNode(rootVal)
            self.incrementPreOrderArrIndex()
            
            if self.getPreOrderArrIndex() < self.sizeOfArr:
                rootNode.left = self.constructBst(self.preorderArr, self.preorderArr[self.getPreOrderArrIndex()], minVal, rootVal, self.sizeOfArr)
            if self.getPreOrderArrIndex() < self.sizeOfArr:
                rootNode.right = self.constructBst(self.preorderArr, self.preorderArr[self.getPreOrderArrIndex()], rootVal, maxVal, self.sizeOfArr)
        
        return rootNode
        
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        self.preorderArr = preorder
        self.preOrderArrIndex = 0
        self.intMin = float('-inf')
        self.intMax = float('inf')
        self.sizeOfArr = len(preorder)
        return self.constructBst(self.preorderArr, self.preorderArr[0], self.intMin, self.intMax, self.sizeOfArr)
        