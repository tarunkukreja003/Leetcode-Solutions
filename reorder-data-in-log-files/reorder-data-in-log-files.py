class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # logs = []
        # letter log = "ID1 jvnjf oigjr ognj"
        # digit log = "frfrfgr6yh4 12 4 5 6"
        
        # can a log have only 1 word? - no min 3
        # can there be 2 spaces in between 2 words - no
        
        # brute force - 2 arrays 1 for letter log, the 
        
        # complexity - mn log(mn)
        
        lDigit =[]
        dLetter1 = []

        for l in logs:
            val = l.split()
            if val[1].isdigit():
                lDigit.append(l)
            else:
                dLetter1.append([val[0],' '.join(val[1:])])
        dLetter1.sort(key = lambda x: (x[1],x[0]))
        ans =[]
        for i in dLetter1:
            ans.append(i[0]+" "+i[1])
        for l in lDigit:
            ans.append(l)

        return ans

        
        
        
        