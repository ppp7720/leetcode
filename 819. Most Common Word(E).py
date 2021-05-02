paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

import re

# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         para = re.findall('[a-z]+',paragraph.lower())
#         h = dict()
#         com = 0
#         res = ''
#         for i in para:
#             if i not in banned:
#                 h[i] = h.get(i,0) + 1
#                 if h[i] > com:
#                     com = h[i]
#                     res = i
#         return res

#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         para = re.findall('[a-z]+',paragraph.lower())
#         h = []
#         for i in set(para):
#             if i not in banned:
#                 h.append([para.count(i),i])
#         h.sort(reverse=1)
#         return h[0][1]