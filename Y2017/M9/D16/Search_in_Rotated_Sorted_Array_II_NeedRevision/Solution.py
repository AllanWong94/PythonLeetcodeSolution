# Reference: https://discuss.leetcode.com/topic/20593/python-easy-to-understand-solution-with-comments
class Solution(object):
    def search(self, nums, target):
        if not nums:
            return False
        lo,hi=0, len(nums)-1
        while lo<=hi:
            mid=lo+(hi-lo)//2
            if nums[mid]==target:
                return True
            while lo<mid and nums[lo]==nums[mid]:
                lo+=1
            if nums[lo]<=nums[mid]:
                if nums[lo]<=target<nums[mid]:
                    hi=mid-1
                else:
                    lo=mid+1
            else:
                if nums[mid]<target<=nums[hi]:
                    lo=mid+1
                else:
                    hi=mid-1
        return False
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """



# Runtime: ms Beats or equals to %





solution = Solution()
print(solution.search([1,1,3,1],3))

