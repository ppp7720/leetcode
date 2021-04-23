class Solution:

    def readBinaryWatch(self, turnedOn: int):
        
        def go(n,cursor,count):
            h = n >> 6
            m = n & 63
            print("{:>10}".format(bin(n)[2:]),cursor,count)
            if h > 11 or m > 59 or count+cursor > 10: return

            if count == 0: a.append("{}:{:02}".format(h,m))

            if cursor < 10 and count > 0:
                go(n | 0 << cursor, cursor + 1, count - 0)
                go(n | 1 << cursor, cursor + 1, count - 1)

        a = []
        
        go(0,0,turnedOn)
        
        return a

print(Solution().readBinaryWatch(2))