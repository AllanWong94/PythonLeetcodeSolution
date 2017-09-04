# Runtime: 116ms Beats or equals to 64%
# Reference: https://discuss.leetcode.com/topic/23871/java-o-n-solution/2
class Solution(object):
    def wiggleSort(self, nums):
        for i in range(len(nums)):
            a=nums[i-1]
            if (i%2)==(a>nums[i]):
                nums[i-1]=nums[i]
                nums[i]=a