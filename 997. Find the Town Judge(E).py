N = 4
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        arr = [[0,0] for _ in range(N)]

        for p,t in trust:
            arr[p-1][0] += 1
            arr[t-1][1] += 1

        for i in range(N):
            if arr[i][0] == 0 and arr[i][1] == N-1:
                return i+1
        
        return -1

    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        h = dict()
        for i in range(1,N+1): h[i] = 0

        for p,t in trust:
            if p in h: del h[p]
            if t in h: h[t] += 1

        for p,t in h.items():
            if t == N-1: return p
        
        return -1