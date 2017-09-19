# Runtime: 35ms Beats or equals to 97%
class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        n,m=len(matrix),len(matrix[0])
        lo,hi=0,n-1
        mid=-1
        while lo<hi:
            mid=lo+(hi-lo)//2
            if matrix[mid][m-1]==target:
                return True
            if matrix[mid][m-1]>target:
                hi=mid
            else:
                lo=mid+1
        if lo==hi:
            if matrix[lo][m-1]==target:
                return True
            mid=lo
        i=mid
        lo,hi=0,m-1
        while lo<hi:
            mid = lo + (hi - lo) // 2
            if matrix[i][mid] == target:
                return True
            if matrix[i][mid] > target:
                hi = mid
            else:
                lo = mid + 1
        return False

        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,50]]








solution = Solution()
print(solution.searchMatrix(matrix,3))

