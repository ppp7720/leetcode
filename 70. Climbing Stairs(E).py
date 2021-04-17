n = 2

# r = []
# def Solution(a):
#     if sum(a) < n:
#         Solution(a+[1])
#         Solution(a+[2])
#     elif sum(a) == n:
#         r.append(a)
# Solution([])

class Solution:
    def climbStairs(self, n: int) -> int:
        steps = {1:1, 2:2}
        if n < 3: return steps[n]
        else:
            i = 3
            while i <= n:
                steps[i] = steps[i-1] + steps[i-2]
                i += 1
        return steps[n]