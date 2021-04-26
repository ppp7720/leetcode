nums = [1,1,1,1]

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        h = Counter(nums)
        res = 0

        for i in h:
            if i+1 in h:
                res = max(res, h.get(i) + h.get(i+1))
                
        return res