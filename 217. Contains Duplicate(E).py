nums = [1,1,1,3,3,4,3,2,4,2]

class Solution:
    def containsDuplicate(self, nums: list()) -> bool:
        return len(nums) != len(set(nums))

    def containsDuplicate2(self, nums: list()) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]: return True
        return False

print(Solution().containsDuplicate2(nums))