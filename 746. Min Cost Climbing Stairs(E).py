cost = [841,462,566,398,243,248,238,650,989,576,361,126,334,729,446,897,953,38,195,679,65,707,196,705,569,275]

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one = two = 0
        for i in range(2,len(cost)+1):
            temp = one
            one = min(one + cost[i-1], two + cost[i-2])
            two = temp
        return one