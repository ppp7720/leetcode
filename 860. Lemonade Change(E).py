bills = [5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]

# class Solution:
#     def lemonadeChange(self, bills: List[int]) -> bool:
#         f = 0
#         t = 0
#         for i in bills:
#             if i == 5:
#                 f += 1
#             elif i == 10:
#                 if f:
#                     f -= 1
#                     t += 1
#                 else: return False
#             else:
#                 if f and t:
#                     f -= 1
#                     t -= 1
#                 elif f > 2:
#                     f -= 3
#                 else: return False
#         return True
