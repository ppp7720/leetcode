from typing import List


arr = [37,12,28,9,100,56,80,5,12]

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = sorted(set(arr))

        h = dict()
        for i, n in enumerate(rank, start=1): h[n] = i

        return [h[n] for n in arr]