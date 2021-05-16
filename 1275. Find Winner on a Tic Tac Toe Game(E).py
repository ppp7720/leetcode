from itertools import combinations
from typing import List

moves = [[1,2],[2,1],[1,0],[0,0],[0,1],[2,0],[1,1]]

class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        win =  [[[0,0],[0,1],[0,2]],
                [[1,0],[1,1],[1,2]],
                [[2,0],[2,1],[2,2]], 
                [[0,0],[1,0],[2,0]], 
                [[0,1],[1,1],[2,1]], 
                [[0,2],[1,2],[2,2]], 
                [[0,0],[1,1],[2,2]], 
                [[0,2],[1,1],[2,0]]]


        for i in combinations(moves[::2],3):
            A = sorted(list(i))
            if A in win: return "A"

        for i in combinations(moves[1::2],3):
            B = sorted(list(i))
            if B in win: return "B"
            
        return "Draw" if len(moves) == 9 else "Pending"

    def tictactoe(self, moves: List[List[int]]) -> str:
        b = [['0']*3 for _ in range(3)]
        res = {'XXX' : 'A', 'OOO' : 'B'}
        
        for r,c in moves[::2]: b[r][c] = 'X'

        for r,c in moves[1::2]: b[r][c] = 'O'

        for i in range(3):
            x = b[i][0] + b[i][1] + b[i][2]
            y = b[0][i] + b[1][i] + b[2][i]
            if x in res: return res[x]
            if y in res: return res[y]

        x = b[0][0] + b[1][1] +b [2][2]
        y = b[0][2] + b[1][1] +b[2][0]
        if x in res: return res[x]
        if y in res: return res[y]
        
        return "Draw" if len(moves) == 9 else "Pending"