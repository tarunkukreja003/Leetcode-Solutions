class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        """
        is it possible that the original array has 0 elements? even if it is return []
        
        if the length of doubled array == odd then return [] because there will be a value for every element of original array and if even 1 is not there then return []
        
        [6,0,3,1] -> not a doubled array
        [1,2,2] -> not a doubled array -> odd length
        
        the original array should be half of the length
        can the elements in the original array be duplicates? -> yes
        
        ------------
        brute-force
        
        [6,0,3,1] 
             ^       
        except the current element
        [3]
        
        if the length of the original array is half then return True
        
        O(n^2)
        O(1)
        
        ---------------------
        [0,1,0,2]
         ^   ^
         
        [1,2,3,2,4,6]
        after sorting
        [1,2,2,3,4,6]
        
        [2,50,20,100,40]
        [2,3,4,20,30,40,50,100]
              ^   
        [50, 51,52....100]
        [0,0,1,2]
           i j
        [50,100,100,100,200,200]
              i j
        [2,4,4,8]
         
        
        once we sort the array:
        we'll start from the 0th index ith pointer
        we'll start a j pointer until <= double of ith element
        
        
        
        nlogn
         we might have to visit some elements mutiple times so it won't improve the complexity
        
        [0,0,1,2] -> 
        
        sorting will help
        
        ----------------------
        hashing 
        
        [0,0,1,2]
        
        decrease the frequency of both -> currelement and twice of the element's frequency by 1
        
        if frequency of curr element is 0 then continue
        
        [0,1]
        {
        0:0
        1:0
        2:0
        }
        
        
        [2,4]
        n*2 ki frequency 0 nhi ho sakti
        {
        2:0
        4:0
        
        }
        if the twice value is not there in the hashmap then just continue
        
        
        
        """
        
        if len(changed) % 2 == 1:
            return []
        

        original = []
        numbers = collections.Counter(changed)
        
        for n in sorted(changed):
            v = n*2
            if numbers[n] > 0 and numbers[v] > 0:
                original.append(n)
                numbers[n] -= 1
                numbers[v] -= 1
            elif n // 2 not in numbers or n % 2 == 1:
                return []
        return original
        
