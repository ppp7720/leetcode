nums = [3,3]
target = 6

class Solution:
    def twoSum(self, nums, target):
        i = 0
        while i <= len(nums):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j]:
                    return(i,j)

A = Solution()
print(A.twoSum(nums,target))
