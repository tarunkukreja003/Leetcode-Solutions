# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        elementsDict = {}
        
        currentNode = head
        previousNode = None
        
        while currentNode:
            if currentNode.val not in elementsDict:
                elementsDict[currentNode.val] = True
                previousNode = currentNode
                currentNode = currentNode.next
                
            else:
                # this is the duplicate element
                # delete the element from the linked list
                
                # it cannot be the first element, since the first element will not be duplicate
                # it can be the last element
                previousNode.next = currentNode.next
                currentNode.next = None
                currentNode = previousNode.next
        
        return head
        
                
        