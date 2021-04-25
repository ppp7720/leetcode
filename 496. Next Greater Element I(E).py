nums1 = [4,1,2]
nums2 = [3,1,2,4]

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        next_greater = dict()
        stack = list()
        answer = list()

        for i in nums2:
            while stack and stack[-1] < i: next_greater[stack.pop()] = i
            stack.append(i)

        for i in nums1:
            if i in next_greater:
                answer.append(next_greater[i])
            else:
                answer.append(-1)
                
        return answer

    def nextGreaterElement2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        next_greater = dict()
        stack = list()
        answer = list()

        for i in nums2:
            while stack and stack[-1] < i: next_greater[stack.pop()] = i
            stack.append(i)

        while stack:
            next_greater[stack.pop()] = -1
                
        return [next_greater[i] for i in nums1]

        
# print(nums1)

# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
#         r = []
        
#         for i in nums1:
        
#             sub = nums2[nums2.index(i)+1:]

#             if not sub or i >= max(sub): r.append(-1)

#             else:
#                 for j in sub:
#                     if j > i:
#                         r.append(j)
#                         break
#         return r
