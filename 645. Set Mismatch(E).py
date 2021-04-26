nums = [1,1]

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        mx = len(nums)
        s = sum(set(nums))
        r = sum(nums) - s
        l = mx*(mx+1)//2 - s
        return [r, l]