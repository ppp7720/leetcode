arr = [2]

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) == 1: return False
        
        inc = 0
        dec = 0
        
        for i in range(1,len(arr)):
            if not dec and arr[i-1] < arr[i]: inc = 1
            elif inc and arr[i-1] > arr[i]: dec = 1
            else: return False
        
        return True if inc and dec else False

    def validMountainArray(self, arr: List[int]) -> bool:
        l = len(arr)-1
        i = 0
        while i < l and arr[i] < arr[i+1]: i += 1
        if i == 0 or i == l: return False
        while i < l and arr[i] > arr[i+1]: i += 1
        return i == l