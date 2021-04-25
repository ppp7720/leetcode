score = [10,3,8,9,4]

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = sorted(score, reverse=1)
        medal = {0 : "Gold Medal",
                 1 : "Silver Medal",
                 2 : "Bronze Medal"}

        h = dict()

        for i, n in enumerate(rank):
            if i in medal: h[n] = medal[i]
            else: h[n] = str(i+1)

        for i, n in enumerate(score):
            score[i] = h[n]
        
        return score
