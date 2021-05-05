deck = [1,2,3,4,4,3,2,1]

from math import gcd
from collections import Counter
from functools import reduce

# class Solution:
#     def hasGroupsSizeX(self, deck: List[int]) -> bool:
#         if len(deck) < 2: return False
      
#         d = set(deck)
#         nd = [deck.count(i) for i in d]
#         test = [i for i in range(2,nd[0]+1) if nd[0]%i == 0]

#         for i in nd:
#             for j in test:
#                 if i % j != 0:
#                     test.remove(j)
#         return len(test) > 0


#     def hasGroupsSizeX(self, deck: List[int]) -> bool:
#         return reduce(gcd,Counter(deck).values()) >= 2