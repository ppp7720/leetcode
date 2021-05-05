nums = [4,2,5,7]

# class Solution:
#     def sortArrayByParityII(self, nums: List[int]) -> List[int]:
#         even = []
#         odd = []
#         for i in nums:
#             if i%2 == 0: even.append(i)
#             else: odd.append(i)
#         ans = []
#         for i in range(len(nums)//2):
#             ans.append(even[i])
#             ans.append(odd[i])
#         return ans

#     def sortArrayByParityII2(self, nums: List[int]) -> List[int]:
#         ans = [None]*len(nums)
#         even = 0
#         odd = 1
#         for i in nums:
#             if i%2 == 0:
#                 ans[even] = i
#                 even += 2
#             else:
#                 ans[odd] = i
#                 odd += 2
#         return ans