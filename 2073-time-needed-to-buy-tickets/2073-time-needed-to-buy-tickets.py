class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        
        
         
         when 0 then leave the line
         
         
         
        time = 0
        tickets[k] = [tickets[k], pos]
        personAtKPosition = tickets[k]
        
        while front <= end and personAtKPosition[0] != 0
        
        if tickets[front] is list:
            personAtKPosition[0] -= 1
            time += 1
            if personAtKPosition[0] == 0:
                break
        
        currTicket -= 1
        time += 1
        
        
        if currTicket == 0:
            front ++
        else:
            append to array currTicket -=1
            front ++
            end ++
        
        
     
         
        time complexity -> O(sum of all the tickets)
        space complexity -> O(t)
        
        
        [1,     2,     [1,pos],      0,        1,     [0,pos],       1]
                                                        front       end
        
        t = 6
        
        
        [[3,pos]]
        front, end
        k = 0
        t = 1
        
        """
        n = len(tickets)
        time = 0
        front = 0
        end = n-1
        tickets[k] = [tickets[k], pos]
        
        while front <= end:
        
            if type(tickets[front]) == list:
                print(tickets[front])
                tickets[front][0] -= 1
                time += 1
                if tickets[front][0] == 0:
                    break
                else:
                    tickets.append(tickets[front]) 
                    front += 1
                    end += 1
            else:
                print(tickets[front])
                tickets[front] -= 1
                time += 1
                if tickets[front] == 0:
                    front += 1
                else:
                    tickets.append(tickets[front]) 
                    front += 1
                    end += 1
                
        
        return time
        
        
        
        