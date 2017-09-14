class Solution(object):
    # Reference: https://discuss.leetcode.com/topic/32861/3-lines-python-with-explanation-proof
    def wiggleSort(self, nums):
        nums.sort()
        half = len(nums[::2]) - 1
        nums[::2], nums[1::2] = nums[half::-1], nums[:half:-1]
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
