s = "a##c"
t = "#a#c"

# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         def go(string):
#             res = []
#             for i in list(string):
#                 if i != '#': res.append(i)
#                 elif res: res.pop()
#             return ''.join(res)
#         return go(s) == go(t)