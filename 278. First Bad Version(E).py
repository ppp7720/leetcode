n = 100
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while r > l:
            m = (l+r)//2
            if isBadVersion(m): r = m
            else: l = m+1
        return l

def firstBadVersion2(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while r >= l:
            m = (l+r)//2
            if isBadVersion(m): r = m-1
            else: l = m+1
        return l+1