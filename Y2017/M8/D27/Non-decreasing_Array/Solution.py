# Runtime: 55ms Beats or equals to 100%
class Solution(object):
    def checkPossibility(self, nums):
        count=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                count+=1
                if count>1 or ((0<i<len(nums)-1 and nums[i-1]>nums[i+1]) and (i<len(nums)-2) and nums[i]>nums[i+2]):
                    return False
        return True


        """
        :type nums: List[int]
        :rtype: bool
        """

