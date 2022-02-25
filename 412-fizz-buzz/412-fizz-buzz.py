class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        [""]
        is i 1-indexed or 0-indexed? -> the former
        
        i will go from 1 to n? -> yes
        
        n = 3
        i = 3
        
        ["1", "2", "Fizz"]
        
        we'll just run a loop and check whether i is divisible by 3, 5
        """
        
        output = []
        
        for i in range(1, n+1):
            if i % 3 == 0 and i%5 == 0:
                output.append("FizzBuzz")
            elif i % 3 == 0:
                output.append("Fizz")
            elif i % 5 == 0:
                output.append("Buzz")
            else:
                output.append(""+str(i))
        return output
            
        