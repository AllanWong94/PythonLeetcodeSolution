# Runtime: 65ms Beats or equals to 43%
class Solution(object):
    def removeDuplicates(self, nums):
        ptr = end = count = 0
        cur = None
        for i in nums:
            if i == cur:
                if count != 2:
                    count += 1
                    ptr += 1
            else:
                cur = i
                count = 1
                if end != ptr:
                    nums[ptr] = i
                ptr += 1
            end += 1
        return ptr

        """
        :type nums: List[int]
        :rtype: int
        """

    # Runtime: 59ms
    # def removeDuplicates(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     prev = None
    #     ctr = 0
    #     i = 0
    #     j = 0
    #     while i < len(nums):
    #         if nums[i] != prev:
    #             prev = nums[i]
    #             ctr = 1
    #         else:
    #             ctr += 1
    #         if ctr <= 2:
    #             nums[j] = nums[i]
    #             j += 1
    #         i += 1
    #     return j
    #
solution = Solution()
nums=[1,1,1,2,2,3]
print(solution.removeDuplicates(nums))
print(nums)
