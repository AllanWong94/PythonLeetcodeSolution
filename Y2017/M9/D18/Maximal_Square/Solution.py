# Runtime: 785ms Beats or equals to 1% Boooooooooo...
class Solution(object):
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        res,count,w,h=0,1,len(matrix[0]),len(matrix)
        for i in range(h):
            for j in range(w):
                if matrix[i][j]=='1':
                    while self.validSquare(matrix,i,j,w,h,count):
                        res=max(res,count*count)
                        count+=1
                    count=1
        return res

    def validSquare(self,matrix,idx1,idx2,w,h,count):
        if idx1+count-1>=h or idx2+count-1>=w:
            return False
        for i in range(idx1,idx1+count):
            for j in range(idx2,idx2+count):
                if matrix[i][j]=='0':
                    return False
        return True
        """
        :type matrix: List[List[str]]
        :rtype: int
        """






matrix=["0001","1101","1111","0111","0111"]

solution = Solution()
print(solution.maximalSquare(matrix))

