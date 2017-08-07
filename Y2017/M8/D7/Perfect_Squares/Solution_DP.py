from math import sqrt


class Solution(object):
    # Runtime: 7055ms Beats or equals to 6%
    # Reference: https://discuss.leetcode.com/topic/24255/summary-of-4-different-solutions-bfs-dp-static-dp-and-mathematics
    def numSquares(self, n):
        if n <= 0: return 0
        cntPerfectSquares=[10*20]*(n+1)
        cntPerfectSquares[0]=0
        for i in range(n+1):
            j=1
            while j**2<=i:
                cntPerfectSquares[i]=min(cntPerfectSquares[i],cntPerfectSquares[i-j**2]+1)
                j+=1
        return cntPerfectSquares[n]


        """
        :type n: int
        :rtype: int
        """



solution = Solution()
print(solution.numSquares(1))

