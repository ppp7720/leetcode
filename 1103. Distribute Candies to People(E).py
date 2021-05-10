candies = 60
num_people = 5

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        l = [0] * num_people
        i = 0
        while candies > i:
            l[i%num_people] += i + 1
            candies -= i + 1
            i += 1
        l[i%num_people] += candies
        return l