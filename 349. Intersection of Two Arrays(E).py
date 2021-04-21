nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1)&set(nums2))

    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        result = []
        if len(num1) > len(nums2):
            for i in nums2:
                if i in nums1: result.append(i)
        else:
            for i in nums1:
                if i in nums2: result.append(i)