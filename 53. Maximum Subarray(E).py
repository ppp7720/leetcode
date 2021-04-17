nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [-2,-1,-2]

lm = 0
gm = nums[0]
for i in nums:
    lm = max(i, i+lm)
    if gm < lm: gm = lm
print(gm)








# if nums == []: print(0)

# else:
#     answer = []

#     # step 1

#     i = 0
#     j = len(nums)
#     r = []

#     while i < j:
#         r.append(sum(nums[i:j]))
#         i += 1
#     i = r.index(max(r))

#     r = []
#     while i < j:
#         r.append(sum(nums[i:j]))
#         j -= 1
#     j = len(nums) - r.index(max(r))

#     answer.append(sum(nums[i:j]))

#     # step 2

#     i = 0
#     j = len(nums)
#     r = []

#     r = []
#     while i < j:
#         r.append(sum(nums[i:j]))
#         j -= 1
#     j = len(nums) - r.index(max(r))

#     r = []
#     while i < j:
#         r.append(sum(nums[i:j]))
#         i += 1
#     i = r.index(max(r))

#     answer.append(sum(nums[i:j]))

# print(max(answer))

#전체탐색
# r = []
# j = 1

# while j <= len(nums):
#     i = 0
#     while i+j < len(nums)+1:
#         r.append(sum(nums[i:i+j]))
#         i += 1
#     j += 1

# print(r)