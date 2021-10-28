# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        
        self.unpackedList = collections.deque()
        self.nestedList = nestedList
        self.recursiveUnpackList(self.nestedList)
        
    def recursiveUnpackList(self, nestedList):
        for nestedInt in nestedList:
            if nestedInt.isInteger():
                self.unpackedList.append(nestedInt.getInteger())
            else:
                # recursive call
                self.recursiveUnpackList(nestedInt.getList())
        
    def next(self) -> int:
        # we will have to pop at the front of unpackedList because we are iterating the elements and putting it in another resulting array res in the same order
        nextElement = self.unpackedList.popleft()
        return nextElement
        
            
        
    
    def hasNext(self) -> bool:
        if self.unpackedList:
            return True
        else:
            return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())