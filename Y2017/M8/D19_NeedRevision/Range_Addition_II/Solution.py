# Runtime: 46ms=>42ms Beats or equals to 53%=>75%   Fastest.
class Solution(object):
    def maxCount(self, m, n, ops):
        return min([i[0] for i in ops])*min(j[1] for j in ops)

        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """


