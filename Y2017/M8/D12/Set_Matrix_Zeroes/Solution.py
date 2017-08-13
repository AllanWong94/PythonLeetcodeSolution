# Runtime: 155ms Beats or equals to 65%
class Solution(object):
    def setZeroes(self, matrix):
        X,Y=set(),set()
        h,w=len(matrix),len(matrix[0])
        for i in range(h):
            for j in range(w):
                if not matrix[i][j]:
                    X.add(j)
                    Y.add(i)

        for i in range(h):
            for j in range(w):
                if j in X or i in Y:
                    matrix[i][j]=0

        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """




mat=[[1,0,3]]

solution = Solution()
print(solution.setZeroes(mat))

