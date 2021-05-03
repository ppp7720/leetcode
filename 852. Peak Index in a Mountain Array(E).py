class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        for i in range(len(arr)):
            if arr[i] > arr[i+1]: return i

    def peakIndexInMountainArray2(self, arr: List[int]) -> int:
        i = 0
        j = len(arr)-1
        while i < j:
            b = (i+j)//2
            if arr[b] > arr[b+1]: j = b
            else: i = b + 1
        return i