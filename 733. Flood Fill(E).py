image = [[0,0,0],[0,1,1]]
sr = 1
sc = 1
newColor = 1


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        def flood_fill(r,c):
            if image[r][c] == t:
                image[r][c] = newColor
                if r: flood_fill(r-1,c)
                if r < len(image)-1: flood_fill(r+1,c)
                if c: flood_fill(r,c-1)
                if c < len(image[0])-1: flood_fill(r,c+1)
        
        t = image[sr][sc]
        if t == newColor: return image
        else: flood_fill(sr,sc)
        return image