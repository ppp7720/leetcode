day = 15
month = 8
year = 1993

from datetime import datetime

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return datetime(year , month , day).strftime('%A')

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        weekday = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]

        days = 0

        for y in range(1971,year):
            if (y%4 == 0 and y%100 != 0) or y%400 == 0: days += 366
            else: days += 365


        mm = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30}
        if (year%4 == 0 and year%100 != 0) or year%400 == 0: mm[2] += 1

        for i in range(1,month):
            days += mm[i]

        days += day-1

        return weekday[days%7]