# Runtime: 39ms Beats or equals to 46% Fastest.
class Solution(object):
    def uniquePaths(self, m, n):
        a,b=m+n-2,min(m,n)-1
        res=1
        for i in range(b):
            res*=a
            a-=1
        for i in range(b,1,-1):
            res/=i
        return res
        """
        :type m: int
        :type n: int
        :rtype: int
        """


