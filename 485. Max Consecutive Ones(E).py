nums = [1,1,0,1,1,1]


r = 0
m = 0
for i in nums:
    if i: r += i
    else: r = 0
    m = max(m,r)
print(2**m)