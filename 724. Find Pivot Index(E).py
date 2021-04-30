nums = [2,1,-1]

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ls = 0
        rs = sum(nums)
        for i, n in enumerate(nums):
            if ls == rs - n: return i
            ls += n
            rs -= n
        return -1

    def pivotIndex2(self, nums: List[int]) -> int:
        ls = 0
        S = sum(nums)
        for i, n in enumerate(nums):
            if ls == S - ls - n: return i
            ls += n
        return -1        