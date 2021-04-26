nums = [1,12,-5,-6,50,3]
k = 4

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = m = sum(nums[:k])
        for i in range(k,len(nums)):
            n += nums[i] - nums[i-k]
            m = max(m,n)
        return m/k