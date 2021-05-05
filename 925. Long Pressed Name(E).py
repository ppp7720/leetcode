name = "laidez"
typed = "laidezcc"

# class Solution:
#     def isLongPressedName(self, name: str, typed: str) -> bool:
#         i = 0
#         j = 0
#         while i < len(name) and j < len(typed):
#             if typed[j] == name[i]:
#                 i += 1
#                 j += 1
#             elif j > 0 and typed[j] == typed[j-1]:
#                 j += 1
#             else:
#                 return False

#         if i != len(name):
#             return False

#         else:
#             while j < len(typed):
#                 if typed[j] != name[-1]:
#                     return False
#                 else:
#                     j += 1
        
#         return True

#     def isLongPressedName(self, name: str, typed: str) -> bool:
#         n = []
#         t = []
#         i = 0
#         count = 1
#         while i < len(name):
#             if i == len(name)-1 or name[i] != name[i+1]:
#                 n.append([name[i],count])
#                 count = 1
#             else:
#                 count += 1
#             i += 1

#         i = 0
#         count = 1
#         while i < len(typed):
#             if i == len(typed)-1 or typed[i] != typed[i+1]:
#                 t.append([typed[i],count])
#                 count = 1
#             else:
#                 count += 1
#             i += 1

#         if len(n) != len(t): return False
#         for a,b in zip(n,t):
#             if a[0] != b[0] or a[1] > b[1]: return False
        
#         return True