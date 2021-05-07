nums = [3,6,2,3]

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        while len(nums) > 2:
            c = nums.pop()
            if nums[-1] + nums[-2] > c:
                return nums[-1] + nums[-2] + c
        return 0