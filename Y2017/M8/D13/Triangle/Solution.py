# Runtime: 42ms Beats or equals to 92% One-time AC! Smooth!
class Solution(object):
    def minimumTotal(self, triangle):
        l=len(triangle)
        for i in range(1,l):
            triangle[i][0]+=triangle[i-1][0]
            triangle[i][i]+=triangle[i-1][i-1]
            for k in range(1,i):
                triangle[i][k]+=min(triangle[i-1][k-1],triangle[i-1][k])
        return min(triangle[l-1])

        """
        :type triangle: List[List[int]]
        :rtype: int
        """

