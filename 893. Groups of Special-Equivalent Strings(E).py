A = ["abcd","cdab","cbad","xyzz","zzxy","zzyx"]

# class Solution:
#     def numSpecialEquivGroups(self, A: List[str]) -> int:
#         _A = []
#         for s in A:
#             c = [sorted(s[::2]),sorted(s[1::2])]
#             if c not in _A: _A.append(c)
#         return len(_A)

#     def numSpecialEquivGroups(self, A: List[str]) -> int:
#         _A = set()
#         for s in A:
#             c = (''.join(sorted(s[::2]))+''.join(sorted(s[1::2])))
#             _A.add(c)
#         return len(_A)
    
# print(_A)