# Runtime: 72ms Beats or equals to 52%
# Reference: https://discuss.leetcode.com/topic/81759/1-liner-in-python-o-n-time
from collections import Counter
class Solution(object):
    def findPairs(self, nums, k):
        if k>0:
            return len(set(nums)&set(n+k for n in nums))
        if k==0:
            return sum([v>1 for v in Counter(nums).values()])
        return 0
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """








solution = Solution()
print(solution.findPairs([1,3,1,5,4],0))

