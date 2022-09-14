class Solution(object):
    from collections import deque
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
        """
        
        is k given? yes, n is also given
        
        k = 2
        
         1
    
    6           2
     
             3
        4
        
        
        finding the time complexity:
        5 + 
        
        nk -> we'll have to traverse k friends to eliminate one person
        for n-1 persons traverse k friends -> nk

        simple queue problem
        
        start k with the front of queue, if k == 0 then pop that element, else move the current element to the back of the queue and decrement k
        
        """
        
        friendsQueue = deque([i for i in range(1,n+1) ])
        
        # print(friendsQueue)
        
        while len(friendsQueue) > 1:
            kTemp = k - 1
            while kTemp != 0:
                frontOfQueue=friendsQueue.popleft()
                friendsQueue.append(frontOfQueue)
                kTemp -= 1
            friendEliminated = friendsQueue.popleft()
            print("friend eliminated", friendEliminated)
        
        return friendsQueue[0]
            
        