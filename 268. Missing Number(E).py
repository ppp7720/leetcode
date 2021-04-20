nums = [3,0,1]

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            if i not in nums:
                return i


    def missingNumber2(self, nums: List[int]) -> int:
        r = len(nums)
        for i, n in enumerate(nums):
            r ^= i^n
        return n


    def missingNumber3(self, nums: List[int]) -> int:        
        return len(nums)*(len(nums)+1)//2 - sum(nums)