list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["KFC","Burger King","Tapioca Express","Shogun"]

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        h = dict()
        mm = 10000
        for i, n in enumerate(list1):
            h[n] = h.get(n,0) + i
        for i, n in enumerate(list2):
            if n in h:
                index = h[n] + i
                if index < mm:
                    res = [n]
                    mm = index
                elif index == mm:
                    res.append(n)
        return res