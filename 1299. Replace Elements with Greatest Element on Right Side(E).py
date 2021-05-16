from typing import List


arr = [17,18,5,4,6,1]

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        res[-1] = -1
        for i in range(len(arr)-2, -1, -1):
            res[i] = max(res[i + 1], arr[i + 1])
        return res