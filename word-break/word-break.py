class Solution:
    def wordBreak(self, T: str, W: List[str]) -> bool:
        
        @cache
        def recur(start):
            
            if start == len(T):
                return True
            
            ans = False
            for w in W:
                end = start + len(w)
                if w == T[start:end]:
                    ans = ans or recur(end)
                    
            return ans
        
        return recur(0) 
        