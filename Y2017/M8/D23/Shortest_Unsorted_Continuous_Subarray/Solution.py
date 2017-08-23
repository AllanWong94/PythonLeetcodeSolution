class Solution(object):
    # TLEed for input of large size.
    # Because of the max and min.
    def findUnsortedSubarray(self, nums):
        lo,hi=0,len(nums)-1
        res=0
        if min(nums[lo:hi+1])==max(nums[lo:hi+1]):
            return 0
        while lo<=hi and nums[lo]<=min(nums[lo:]):
            lo+=1
        while lo<=hi and nums[hi]>=max(nums[:hi+1]):
            hi-=1
        res=hi-lo+1
        return res
        """
        :type nums: List[int]
        :rtype: int
        """



# Runtime: ms Beats or equals to %





solution = Solution()
print(solution.findUnsortedSubarray([2,6,4,8,10,9,15])) #5

print(solution.findUnsortedSubarray([1,2,3,4])) #0

print(solution.findUnsortedSubarray([2,1])) #2
