# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        powerOf10 = 0
        
        currentNodel1, currentNodel2 = l1, l2
        number1, number2 = 0, 0
        
        while currentNodel1:
            
            number1 +=  currentNodel1.val * 10**powerOf10
            powerOf10 += 1
            currentNodel1 = currentNodel1.next
        
        powerOf10 = 0
        
        while currentNodel2:
            
            number2 +=  currentNodel2.val * 10**powerOf10
            powerOf10 += 1
            currentNodel2 = currentNodel2.next
            
            
        # print(number1)
        # print(number2)
        
        resultingSum =  number1 + number2
        # print(resultingSum)
        
        
        ## deconstruct the resultingSum from unit's place and store it in linked list
        
        resultingLinkedList = ListNode()
        resultingLinkedListHead = resultingLinkedList
        
        while resultingSum != 0:
            currentDigit = resultingSum % 10
            resultingLinkedList.val = currentDigit
            print(resultingLinkedList)
            resultingSum = resultingSum // 10
            if resultingSum == 0:
                break
            # print(resultingSum)
            resultingLinkedList.next = ListNode()
            resultingLinkedList = resultingLinkedList.next
        
        return resultingLinkedListHead
        
            
        
            
            
        