class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        """
        
        very good greedy problem
        
        this makes us realise what greedy problem is
        
        if we encounter I or D how do we know what to number to pick for the curr position in perm?
        
        let's take some egs.
        
        "IDI"
        here the middle will be the max
        [0,3,1,2]
        
        "DIII"
        [4,0,1,2,3]
        here the first will be the max
        
        "DDDD"
        [4,3,2,1,0]
        
        here the first will be the max
        
        "IIII"
        [0,1,2,3,4]
        
        here the last will be the max
        
        "IDDD"
        [0,4,3,2,1]
        
        
        
        if we encounter the first "D" we know it has to be greater than i+1 and looking at the examples above we know D will hold the max value that is possible and I will hold the minimum value possible and since all values in perm will be unique we maintain maxRemaining and minRemaining which means the max value that is not used and is possible for the curr perm index and similarly for minRemaining
        
        when we reach perm[-1] maxRemaining will become equal to minRemaining and that will be the value of perm[-1]
        
        
        
        maxLeft = 2
        minLeft = 2
        
        if s[i] = "D":
            maxLeft
            maxLeft -= 1
        
        
        [0,4,1,3,2]
        
        s[0] == "D" -> then perm[0] = N
        s[0] == "I" -> then perm[0] = 0
        
        
        
        
        
        i = 0
        currNumber = perm[i]
        
        if s[i] == 'I':
            if s[i+1] == 'I':
                perm[i+1] = currNumber + 1
            
        
        """
        
        i = 0
        n = len(s)
        
        maxRemaining = n
        minRemaining = 0
        
        perm = [0 for _ in range(n+1)]
        
        
        
        for i in range(n):
            if s[i] == "D":
                perm[i] = maxRemaining
                maxRemaining -= 1
            elif s[i] == "I":
                perm[i] = minRemaining
                minRemaining += 1
        
        perm[-1] = minRemaining
        
        return perm
        