# Runtime: 36ms Beats or equals to 83% One-time AC.
# Two-pass solution.
class Solution(object):
    def sortColors(self, nums):
        index=[nums.count(0),nums.count(1),nums.count(2)]
        index[1]+=index[0]
        index[2]+=index[1]
        for i in range(index[0]):
            nums[i]=0
        for i in range(index[0],index[1]):
            nums[i]=1
        for i in range(index[1],len(nums)):
            nums[i]=2






        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """








solution = Solution()
print(solution)
