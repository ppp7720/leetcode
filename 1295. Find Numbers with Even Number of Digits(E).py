from typing import List


nums = [12,345,2,6,7896]

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            if len(str(n))%2 == 0:
                res += 1
        return res