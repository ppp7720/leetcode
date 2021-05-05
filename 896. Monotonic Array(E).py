A = [6,5,4,4]

# class Solution:
#     def isMonotonic(self, A: List[int]) -> bool:
#         return A == sorted(A) or A == sorted(A, reverse=1)

#     def isMonotonic(self, A: List[int]) -> bool:
#         inc = 1
#         dec = 1
#         for i in range(len(A)-1):
#             if A[i] > A[i+1]: inc = 0
#             if A[i] < A[i+1]: dec = 0
#         return inc or dec