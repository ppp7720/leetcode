arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        h = dict()
        
        for i, n in enumerate(arr2): h[n] = i
            
        arr1.sort()
        
        arr1.sort(key=lambda x: (h.get(x,10000),x) )
        
        return arr1

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        h = dict()
        
        for i, n in enumerate(arr2): h[n] = i
        
        arr1.sort(key=lambda x: (h.get(x,10000),x) )
        
        return arr1