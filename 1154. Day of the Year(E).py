date = "2008-10-10"

class Solution:
    def dayOfYear(self, date: str) -> int:
        
        y, m, d = map(int,date.split('-'))

        mm = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30}

        if (y%4 == 0 and y%100 != 0) or y%400 == 0:
            mm[2] += 1

        day = 0

        for i in range(1,m):
            day += mm[i]

        return day+d