nums = [1,3,5,4,2,3,4,5]

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 0
        if nums:
            r = 1
            ans = 1
            for i in range(1,len(nums)):
                if nums[i] > nums[i-1]: r += 1
                else: r = 1
                ans = max(ans, r)
        return ans