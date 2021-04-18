nums = [4,1,2,1,2]


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a


# List operation
# for i in nums:
#     if nums.count(i) == 1: print(i)

# Hash table
# h = dict()
# for i in nums:
#     if i in h: h[i] += 1
#     else: h[i] = 1
# for i in h:
#     if h[i] == 1: print(i)

# Math
# n = sum(set(nums))*2 - sum(nums)

# Bit(xor)
# a = 0
# for i in nums:
#     a ^= i
# print(a)