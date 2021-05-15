from typing import List


arr = [-3,0,1,-3,1,1,1,-3,10,0]

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        h = set(arr)
        c = set()

        for i in h:
            n = arr.count(i)
            if n in c: return False
            else: c.add(n)
        
        return True

print( Solution().uniqueOccurrences(arr) )