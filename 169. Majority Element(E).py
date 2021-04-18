nums = [2,2,1,1,1,2,2]

class Solution:
    def majorityElement(self, nums: list()) -> int:
        major = 0
        count = 0
        for i in set(nums):
            if nums.count(i) > count:
                count = nums.count(i)
                major = i
        return major


    def majorityElement2(self, nums: list()) -> int:
        nums.sort()
        return nums[(len(nums)-1)//2]

    def majorityElement3(self, nums: list()) -> int:
        candidate = None
        count = 0
        for i in nums:
            if count == 0: candidate = i
            count += (1 if i == candidate else -1)
        return candidate

print(Solution().majorityElement3(nums))