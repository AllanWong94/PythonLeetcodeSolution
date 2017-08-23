class Solution(object):
    def findUnsortedSubarray(self, nums):
        beg,end=-2,-3
        minE,maxE=nums[-1],nums[0]
        for i in range(len(nums)):
            maxE=max(maxE,nums[i])
            minE=min(minE,nums[-1-i])
            if nums[i]<maxE:
                end=i
            if nums[-1-i]>minE:
                beg=len(nums)-i-1
        return end-beg+1



# Runtime: 129ms Beats or equals to 23%
# Reference: https://discuss.leetcode.com/topic/89282/java-o-n-time-o-1-space





solution = Solution()
print(solution.findUnsortedSubarray([2,6,4,8,10,9,15])) #5

print(solution.findUnsortedSubarray([1,2,3,4])) #0

print(solution.findUnsortedSubarray([2,1])) #2
