# Runtime: 48ms Beats or equals to 97% One-time AC!

class Solution(object):
    def arrangeCoins(self, n):
        return int((2*n+0.25)**0.5-0.5)
        """
        :type n: int
        :rtype: int
        """

