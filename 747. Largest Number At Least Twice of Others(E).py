nums = [1,2,3,4]

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        n = sorted(nums)
        l = n.pop()
        if n and l >= n[-1]*2: return nums.index(l)
        else: return -1