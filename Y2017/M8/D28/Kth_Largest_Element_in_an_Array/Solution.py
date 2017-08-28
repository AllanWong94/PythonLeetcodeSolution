# Runtime: 45ms Beats or equals to 78% Fastest.
class Solution(object):
    def findKthLargest(self, nums, k):
        # res = []
        # for i in nums:
        #     res.append(i)
        #     if len(res) > 1:
        #         for j in range(len(res) - 1, 0, -1):
        #             if res[j] < res[j - 1]:
        #                 res[j], res[j - 1] = res[j - 1], res[j]
        #             else:
        #                 break
        return sorted(nums)[-k]
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """






solution = Solution()
print(solution.findKthLargest([3,2,1,5,6,4],2))

