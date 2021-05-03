rec1 = [-1,0,1,1]
rec2 = [0,-1,0,1]

# class Solution:
#     def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
#         if not(rec2[0] >= rec1[2] or rec2[2] <= rec1[0]  or  rec2[1] >= rec1[3] or rec2[3] <= rec1[1]):
#             return not(rec1[0] == rec1[2] or rec1[1] == rec1[3] or rec2[0] == rec2[2] or rec2[1] == rec2[3])

#     def isRectangleOverlap2(self, rec1: List[int], rec2: List[int]) -> bool:
#         return max(rec1[0],rec2[0]) < min(rec1[2],rec2[2]) and max(rec1[1],rec2[1]) < min(rec1[3],rec2[3])