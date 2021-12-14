"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # [{id: , importance: , subordinates: []}]
        
        # we'll be doing BFS
        # we'll have to make a hash table of ids and value will be a tuple in which first value will be their cost and the second value will be their list of subordinates
        # {
        #     1: (5, [2,3]),
        #     2: (3, []),
        #     3: (3, [])
        # }
        
        # initially the queue will have the id provided
        # then we'll pop that and add its value
        # then we'll append to it its subordinates -> we'll go over every subordinate in the list
        # we'll repeat until queue is empty
        
        idToImpAndSubordinatesDict = {}
        totalImportance = 0
        for employee in employees:
            if employee.id not in idToImpAndSubordinatesDict:
                idToImpAndSubordinatesDict[employee.id] = (employee.importance, employee.subordinates)
        # print(idToImpAndSubordinatesDict)
        
        q = collections.deque([id])
        
        while q:
            employeeId = q.popleft()
            totalImportance += idToImpAndSubordinatesDict[employeeId][0]
            
            if idToImpAndSubordinatesDict[employeeId][1]:
                for subordinateId in idToImpAndSubordinatesDict[employeeId][1]:
                    q.append(subordinateId)
        return totalImportance
            
        
        