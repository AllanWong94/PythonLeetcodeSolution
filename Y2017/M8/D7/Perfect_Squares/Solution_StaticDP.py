class Solution(object):

    _cntPerfectSquares = [0]

    # Runtime: 225ms Beats or equals to 86%
    # Reference: https://discuss.leetcode.com/topic/24255/summary-of-4-different-solutions-bfs-dp-static-dp-and-mathematics
    def numSquares(self, n):
        if n <= 0: return 0
        while len(self.cntPerfectSquares) <= n:
            i, l, cnt = 1, len(self.cntPerfectSquares), 10 ** 20
            while i ** 2 <= l:
                cnt = min(cnt, self.cntPerfectSquares[l - i ** 2] + 1)
                i += 1
            self.cntPerfectSquares.append(cnt)
        return self.cntPerfectSquares[n]

        """
        :type n: int
        :rtype: int
        """


solution = Solution()
print(solution.numSquares(1))
