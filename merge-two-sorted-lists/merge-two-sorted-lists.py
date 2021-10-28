# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # we'll maintain a pointer in both the linked list, each pointer initialized to head of the linked list
        
        # print(l1)
        
        resultingLL = ListNode()
        resultingLLHead = resultingLL
        
        self.ll1CurrentNode = l1
        self.ll2CurrentNode = l2
        
        while (self.ll1CurrentNode != None) and (self.ll2CurrentNode != None):
            if self.ll2CurrentNode.val > self.ll1CurrentNode.val:
                resultingLL.next = self.ll1CurrentNode
                resultingLL = resultingLL.next
                self.ll1CurrentNode = self.ll1CurrentNode.next
            else:
                resultingLL.next = self.ll2CurrentNode
                resultingLL = resultingLL.next
                self.ll2CurrentNode = self.ll2CurrentNode.next
        
        while self.ll1CurrentNode != None:
            resultingLL.next = self.ll1CurrentNode
            resultingLL = resultingLL.next
            self.ll1CurrentNode = self.ll1CurrentNode.next
        
        while self.ll2CurrentNode != None:
            resultingLL.next = self.ll2CurrentNode
            resultingLL = resultingLL.next
            self.ll2CurrentNode = self.ll2CurrentNode.next
        
        # remove the first element of resultingLL
        firstElement = resultingLLHead
        resultingLLHead = resultingLLHead.next
        firstElement.next = None
        
        return resultingLLHead
        
        
                
            
            
            
        