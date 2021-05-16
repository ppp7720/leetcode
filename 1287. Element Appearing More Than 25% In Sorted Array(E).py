from typing import List
from collections import Counter

arr = [1,2,2,6,6,6,6,7,10,5,2,6,1,23,5,2,3,6,2,7,2]


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        arr = Counter(arr)
        return max(arr, key=lambda x: arr[x])