# Runtime: 119ms Beats or equals to 56% One-time AC!
class Solution(object):
    def wiggleSort(self, nums):
        nums.sort()
        ptr=1
        while ptr<len(nums)-1:
            nums[ptr],nums[ptr+1]=nums[ptr+1],nums[ptr]
            ptr+=2


        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """


