class Solution:
    def validPalindrome(self, s: str) -> bool:
        # 'abddbba'
        
        # we'll check from left end and right end whether those chars are same or not. If they are we'll just move left+1 and right-1 to check the next pair, if they are not we can move either of them and continue the process until we get False or the whole string is traversed(true)
        
        self.count = 0
        def dfsCheckPalindrome(left, right):
            
            if left <= right:
                if s[left] == s[right]:
                    return dfsCheckPalindrome(left+1, right-1)
                else:
                    self.count += 1
                    print(self.count)
                    if self.count >= 2:
                        return False
                    else:
                        movingRight = dfsCheckPalindrome(left+1, right)
                        movingLeft = dfsCheckPalindrome(left, right-1)
                        print(movingRight)
                        print(movingLeft)
                        return movingRight or movingLeft
            
            
            else:
                print(left, right)
                return True
            
            
                    
        
        
        
        left = 0
        right = len(s)-1
        
        return dfsCheckPalindrome(left, right)
        
        
            
        
        