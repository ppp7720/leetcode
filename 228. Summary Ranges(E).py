class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        r = []
        a = ""
        for i, n in enumerate(nums):
            if a == "": a = n
            try:
                if i == len(nums)-1 or nums[i+1] - n > 1:
                    if a == n: r.append(str(a))
                    else: r.append(str(a)+"->"+str(n))
                    a = ""
            except: continue
        return r