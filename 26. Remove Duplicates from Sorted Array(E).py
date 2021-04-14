nums = []

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        if nums != []:
            s = nums[0]
            while s <= nums[-1]:
                if s in nums:
                    nums[i] = s
                    i += 1
                    s += 1

    def removeDuplicates2(self, nums: List[int]) -> int:
        l = 0
        if nums != []:
            l = 1
            n = nums[0]
            for s in nums:
                if s != n:
                    nums[l] = s
                    l += 1
                    n = s

    def removeDuplicates3(self, nums: List[int]) -> int:
        l = 0
        if nums != []:
            l = 1
            for i in range(1, len(nums)):
                if nums[i-1] != nums[i]:
                    nums[l] = nums[i]
                    l += 1
        return l