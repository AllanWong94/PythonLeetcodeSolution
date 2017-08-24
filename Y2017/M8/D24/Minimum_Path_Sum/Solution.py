# Runtime: 59ms Beats or equals to 65% One-time AC! Fastest and constant space.
class Solution(object):
    def minPathSum(self, grid):
        w,h=len(grid[0]),len(grid)
        for i in range(h):
            for j in range(w):
                if i==0 and j==0:
                    continue
                if i==0:
                    grid[i][j]+=grid[i][j-1]
                elif j==0:
                    grid[i][j]+=grid[i-1][j]
                else:
                    grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]


        """
        :type grid: List[List[int]]
        :rtype: int
        """
