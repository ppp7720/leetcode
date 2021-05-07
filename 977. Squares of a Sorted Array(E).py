nums = [-4,-1,0,3,10]

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(i*i for i in nums)