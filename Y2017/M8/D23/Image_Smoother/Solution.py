# Runtime: 602ms Beats or equals to 91%
class Solution(object):
    def imageSmoother(self, M):
        h,w=len(M),len(M[0])
        new_M=[[0]*w for i in range(h)]
        for i in range(h):
            for j in range(w):
                res=M[i][j]
                cell=1
                if i>0:
                    cell+=1
                    res+=M[i-1][j]
                    if j>0:
                        cell+=1
                        res+=M[i-1][j-1]
                    if j<w-1:
                        cell+=1
                        res+=M[i-1][j+1]
                if i<h-1:
                    cell+=1
                    res+=M[i+1][j]
                    if j>0:
                        cell+=1
                        res+=M[i+1][j-1]
                    if j<w-1:
                        cell+=1
                        res+=M[i+1][j+1]
                if j>0:
                    cell+=1
                    res+=M[i][j-1]
                if j<w-1:
                    cell+=1
                    res+=M[i][j+1]
                new_M[i][j]=int(res/cell)
        return new_M




        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """







solution = Solution()
print(solution.imageSmoother([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]))

