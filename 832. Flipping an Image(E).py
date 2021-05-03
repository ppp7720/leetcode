image = [[1,1,0],[1,0,1],[0,0,0]]

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[1^j for j in i[::-1]] for i in image]