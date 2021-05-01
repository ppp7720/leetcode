jewels = "aA"
stones = "aAAbbbb"

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        for i in stones:
            if i in jewels:
                ans += 1
        return ans

    def numJewelsInStones2(self, jewels: str, stones: str) -> int:
        ans = 0
        for i in jewels: ans += stones.count(i)
        return ans