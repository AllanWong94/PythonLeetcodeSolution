class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        # Runtime: 85ms Beats or equals to 71%
        # Actually fastest.
        count,maxL=0,-1
        for i in nums:
            if i:
                count+=1
            else:
                if count>0:
                    maxL=max(count,maxL)
                count=0
        maxL=max(count,maxL)
        return maxL
        """
        :type nums: List[int]
        :rtype: int
        """
