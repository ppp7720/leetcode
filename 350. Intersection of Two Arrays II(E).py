nums1 = [1,2,2,1]
nums2 = [2,2]

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        result = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]: i += 1
            elif nums1[i] > nums2[j]: j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1
        
        return result

    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:

        map1, map2 = {}, {}
        result = []

        for n in nums1: map1[n] = map1.get(n, 0) + 1

        for n in nums2: map2[n] = map2.get(n, 0) + 1

        for n in map2: result += [n] * min(map2[n], map1.get(n, 0))
        
        return result