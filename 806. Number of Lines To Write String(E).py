widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
s = "bbbcccdddaaa"

# class Solution:
#     def numberOfLines(self, widths: List[int], s: str) -> List[int]:
#         w = dict(zip(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#                       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],widths))

#         lines = 1
#         pixels = 0
#         for i in s:
#             pixels += w[i]
#             if pixels > 100:
#                 lines += 1
#                 pixels = w[i]
#         return [lines, pixels]
