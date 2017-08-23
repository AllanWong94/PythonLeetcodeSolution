class Solution(object):
    # Runtime: 65ms
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                l = i
                break
        if l == None:
            return 0
        r = None
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < nums[i - 1]:
                r = i
                break
        unsorted = nums[l:r+1]
        small, big = min(unsorted), max(unsorted)
        while l > 0 and nums[l - 1] > small:
            l -= 1;
        while r < len(nums) - 1 and nums[r + 1] < big:
            r += 1;
        return r - l + 1