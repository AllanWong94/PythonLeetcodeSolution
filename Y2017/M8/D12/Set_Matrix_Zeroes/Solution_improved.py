# Runtime: 142ms Beats or equals to 96%
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
            if i in X:
                matrix[i]=[0]*w
            else:
                for j in Y:
                    matrix[i][j]=0

        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """




mat=[[1,0,3]]

solution = Solution()
print(solution.setZeroes(mat))

