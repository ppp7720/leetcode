nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        while i < n:
            nums1[m+i] = nums2[i]
            i += 1
        nums1.sort()
        return nums1