nums = [0,1,2,2,3,0,4,2]
val = 2

l = len(nums) - nums.count(val)
i = 0
for n in nums:
    if n != val:
        nums[i] = n
        i += 1
        
print(nums)
        
