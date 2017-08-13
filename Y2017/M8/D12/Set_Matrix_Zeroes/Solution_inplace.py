# Runtime: 155ms Beats or equals to 65%
class Solution(object):
    def setZeroes(self, matrix):
        h,w=len(matrix),len(matrix[0])
        for i in range(h):
            for j in range(w):
                if matrix[i][j]==0:
                    for m in range(h):
                        if matrix[m][j]:
                            matrix[m][j]=None
                    for n in range(w):
                        if matrix[i][n]:
                            matrix[i][n]=None   
        for i in range(h):
            for j in range(w):
                if not matrix[i][j]:
                    matrix[i][j]=0

        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """


mat=[[0,1]]

solution = Solution()
print(solution.setZeroes(mat))



