class Solution(object):
    # Runtime: 279ms Beats or equals to 86%
    # Reference: https://discuss.leetcode.com/topic/64979/python-o-n-time-o-1-space
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x)-1] *= -1
        return res