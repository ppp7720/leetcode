nums = [1,3,5,6]
target = 5

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] >= target: break
            else: i += 1
        return i 
    
    def searchInsert2(self, nums: List[int], target: int) -> int:
        nums.append(target)
        nums.sort()
        return nums.index(target)

    