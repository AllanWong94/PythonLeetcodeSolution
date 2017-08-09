class Solution(object):
    # Runtime: 32ms Beats or equals to 97%
    def findPeakElement(self, nums):
        lo, hi = 0, len(nums) - 1
        while True:
            mid = (lo + hi) // 2
            left, right = mid == 0 or nums[mid] > nums[mid - 1], mid == len(nums)-1 or nums[mid] > nums[mid + 1]
            if left and right:
                return mid
            elif not left and right:
                hi = mid - 1
            else:
                lo = mid + 1


        """
        :type nums: List[int]
        :rtype: int
        """







solution = Solution()
print(solution.findPeakElement([1, 2, 3, 1]))
