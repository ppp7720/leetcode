candyType = [1,1,2,2,3,3]

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType)//2,len(set(candyType)))