import sys
import math
sys.setrecursionlimit(10**6)
class Solution:
    
    def isPowerOfFour(self, num: int) -> bool:
        ### using log
        if num <= 0:
            return False
        return math.log(num, 4).is_integer()
        #### using recursion
        # if num == 1:
        #     return True
        # if (num % 4) != 0:
        #     return False
        # num = num / 4
        # return self.isPowerOfFour(num)

if __name__ == "__main__":
    solutionObj = Solution()
    num = int(input())
    print(solutionObj.isPowerOfFour(num))