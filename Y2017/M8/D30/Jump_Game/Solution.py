# Runtime: 42ms Beats or equals to 91% One-time AC!
class Solution(object):
    def canJump(self, nums):
        if len(nums)==1:
            return True
        start = len(nums)-1
        for i in range(start)[::-1]:
            if nums[i]>0:
                if start-i<=nums[i]:
                    nums[i]*=-1
                    start=i
        return nums[0]<0





        """
        :type nums: List[int]
        :rtype: bool
        """






solution = Solution()
print(solution.canJump([2,3,1,1,4]))

print(solution.canJump([3,2,1,0,4]))
