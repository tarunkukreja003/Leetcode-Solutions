# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we'll have to keep track of node which is 2 steps before as well
        # [1,2,3,3,3,3,4,4,5]
        # duplicateNode = head
        twoStepsBeforeNode = None
        currentNode = head
        previousNode = None
        valDict = {}
        
        while currentNode:
            if currentNode.val not in valDict:
                valDict[currentNode.val] = 1
                twoStepsBeforeNode = previousNode
                previousNode = currentNode
                currentNode = currentNode.next
                # duplicateNode = currentNode
                
            else:
                # now we'll not update twoStepsBeforeNode and this else part will execute until the val has not changed 
                
                ## this logic works only for sorted list
                # print(previousNode)
                while (currentNode) and (previousNode.val == currentNode.val):
                    valDict[currentNode.val] += 1
                    previousNode = currentNode
                    currentNode = currentNode.next
                
                if twoStepsBeforeNode:
                    twoStepsBeforeNode.next = currentNode
                    previousNode.next = None
                    previousNode = twoStepsBeforeNode
                else:
                    # this means we are deleting the initial elements which are duplicates and twoStepsBeforeNode is None
                    head = currentNode
                    previousNode.next = None
                    previousNode = None
                    
                
        return head   
            
            