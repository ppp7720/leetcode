nums1 = [2]
nums2 = []

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums = nums1 + nums2
        nums.sort()
        l = len(nums)
        m = nums[l//2]
        if l%2 == 0:
            return (m + nums[(l//2)-1])/2
        else:
            return m

a = Solution()
print(a.findMedianSortedArrays(nums1,nums2))