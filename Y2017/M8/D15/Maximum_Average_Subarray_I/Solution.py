# Runtime: 335ms=>282ms=>259ms Beats or equals to 15%=>33%=>45%(Actually fastest)
# Improvement: float() is slower than *1.0!
# Improvement: while i<len(nums) is slower than for i in range(len(nums)-k)!
class Solution(object):
    def findMaxAverage(self, nums, k):
        curSum=sum(nums[:k])
        maxAver=curSum*1.0/k
        for i in range(len(nums)-k):
            curSum+=nums[i+k]-nums[i]
            maxAver=max(curSum*1.0/k,maxAver)
        return maxAver

        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """








solution = Solution()
print(solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4))

