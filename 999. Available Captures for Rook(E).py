board = [[".",".",".",".",".",".",".","."],
         [".",".",".","p",".",".",".","."],
         [".",".",".","p",".",".",".","."],
         ["p","p",".","R",".","p","B","."],
         [".",".",".",".",".",".",".","."],
         [".",".",".","B",".",".",".","."],
         [".",".",".","p",".",".",".","."],
         [".",".",".",".",".",".",".","."]]


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for r in range(8):
            if "R" in board[r]:
                R = r
                C = board[r].index("R")
                break

        res = 0

        n = 1
        while C - n >= 0:
            if board[R][C-n] == "p" :
                res += 1
                break
            elif board[R][C-n] == "B": break
            else: n += 1

        n = 1
        while C + n < 8:
            if board[R][C+n] == "p" :
                res += 1
                break
            elif board[R][C+n] == "B": break
            else: n += 1

        n = 1
        while R - n >= 0:
            if board[R-n][C] == "p" :
                res += 1
                break
            elif board[R-n][C] == "B": break
            else: n += 1

        n = 1
        while R + n < 8:
            if board[R+n][C] == "p" :
                res += 1
                break
            elif board[R+n][C] == "B": break
            else: n += 1
        
        return res



# class Solution:
#     def numRookCaptures(self, board: List[List[str]]) -> int:
#         for r in range(8):
#             for c in range(8):
#                 if board[r][c] == "R":
#                     R = r
#                     C = c
#                     break

#         res = 0

#         n = 1
#         while C - n >= 0:
#             if board[R][C-n] == "p" :
#                 res += 1
#                 break
#             elif board[R][C-n] == "B": break
#             else: n += 1

#         n = 1
#         while C + n < 8:
#             if board[R][C+n] == "p" :
#                 res += 1
#                 break
#             elif board[R][C+n] == "B": break
#             else: n += 1

#         n = 1
#         while R - n >= 0:
#             if board[R-n][C] == "p" :
#                 res += 1
#                 break
#             elif board[R-n][C] == "B": break
#             else: n += 1

#         n = 1
#         while R + n < 8:
#             if board[R+n][C] == "p" :
#                 res += 1
#                 break
#             elif board[R+n][C] == "B": break
#             else: n += 1
        
#         return res