# Runtime: 39ms Beats or equals to 81% Fastest.
class Solution(object):
    def generateMatrix(self, n):
        res=[[0]*n for i in range(n)]
        count=1
        right=down=n
        i,j=0,-1
        left=up=-1

        while True:
            for k in range(j+1,right):
                res[i][k]=count
                count+=1
            if count==n*n+1:
                return res
            up+=1
            j=right-1
            for k in range(i+1,down):
                res[k][j]=count
                count+=1
            right-=1
            i=down-1
            for k in range(j-1,left,-1):
                res[i][k]=count
                count+=1
            if count==n*n+1:
                return res
            down-=1
            j=left+1
            for k in range(i-1,up,-1):
                res[k][j]=count
                count+=1
            left+=1
            i=up+1






        """
        :type n: int
        :rtype: List[List[int]]
        """






solution = Solution()
print(solution.generateMatrix(4))

