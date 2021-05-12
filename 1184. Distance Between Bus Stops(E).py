distance = [7,10,1,12,11,14,5,0]
start = 7
destination = 2

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        s = sum(distance[start:destination])
        return min(sum(distance)-s,s)