class Solution(object):
    #Runtime: 32ms Beats or equals to 88%
    #Reference: https://discuss.leetcode.com/topic/24632/python-solution-with-explanation/2
    def numWays(self, n, k):
        if n==0:
            return 0
        if n==1:
            return k
        same, dif=k, k*(k-1)
        for i in range(3, n+1):
            same, dif=dif, (same+dif)*(k-1)
        return same+dif


        """
        :type n: int
        :type k: int
        :rtype: int
        """
