# Runtime: 262ms Beats or equals to 11%
from collections import Counter

class Solution(object):
    def findLHS(self, nums):
        if not nums:
            return 0
        c=Counter(nums)
        appearance=c.most_common()
        if len(appearance)==1:
            return 0
        if abs(appearance[0][0]-appearance[1][0])==1:
            return appearance[0][1]+appearance[1][1]
        maxLength=0
        appearance.sort()
        for i in range(len(appearance)-1):
            if appearance[i+1][0]-appearance[i][0]==1:
                maxLength=max(maxLength,appearance[i+1][1]+appearance[i][1])
        return maxLength
        """
        :type nums: List[int]
        :rtype: int
        """







solution = Solution()
print(solution.findLHS([1,2,2,2,3,4,5,6,4,3,3,5]))

