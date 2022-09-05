class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        
        circular -> 0
        square->1
        
        
        if # of 0's == # of 1's then return 0
        
        
        stop when top of stack == 0 and all the elements in the queue == 1 or vica-versa
        
        O(n^2) solution
        
         students = [1,      1,   1,    0,   0,  1,   1,   1,   1,   1], 
                                                         front      end
                    
                     
         sandwiches = [1,    0  ,0,  0,1,1]
                                   top
        
        while front <= end:
        
            if front == top:
                top += 1
                front += 1

            elif front != top:
                students.append(students[front])
                numberOfStudentsSeenTopSandwich += 1
                if numberOfStudentsSeenTopSandwich == end-front+1:
                    return end-front+1
                front += 1
                end += 1
        
                     
        """
        front = 0
        end = len(students) - 1
        top = 0
        numberOfStudentsSeenTopSandwich = 0
        
        while front <= end:
        
            if students[front] == sandwiches[top]:
                top += 1
                front += 1
                numberOfStudentsSeenTopSandwich = 0

            elif students[front] != sandwiches[top]:
                students.append(students[front])
                numberOfStudentsSeenTopSandwich += 1
                if numberOfStudentsSeenTopSandwich == end-front+1:
                    return end-front+1
                front += 1
                end += 1
        
        return numberOfStudentsSeenTopSandwich
        