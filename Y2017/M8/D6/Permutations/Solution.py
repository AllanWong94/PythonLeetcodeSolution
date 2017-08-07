class Solution(object):
    # def permute(self, nums):
    #     res = []
    #     # Runtime: 76ms Beats or equals to 37%
    #     if len(nums) == 1:
    #         res.append(nums[0])
    #         return res
    #     for i in range(len(nums)):
    #         nums_ = nums[:i] + nums[i + 1:]
    #         list = self.permute(nums_)
    #         for k in list:
    #             if len(list) == 1:
    #                 temp = [nums[i], k]
    #             else:
    #                 temp = [nums[i]] + k
    #             res.append(temp)
    #     return res
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    #
    # Runtime: 55ms
    # def permute(self, nums):
    #     """
    #    :type nums: List[int]
    #          :rtype: List[List[int]]
    #    """
    #     if len(nums) <= 1:
    #         return [nums]
    #     result = []
    #     for perm in self.permute(nums[1:]):
    #         for i in range(len(perm) + 1):
    #             result.append(perm[:i] + [nums[0]] + perm[i:])
    #     return result


solution = Solution()
print(solution.permute([1, 2, 3, 4]))
