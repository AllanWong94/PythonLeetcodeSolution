# Runtime: 539ms Beats or equals to 15%
class Solution(object):
    # # DP.
    # # Reference: https://discuss.leetcode.com/topic/23893/my-expressive-python-solution/2
    # def nthUglyNumber(self, n):
    #     ugly = [1]
    #     i2, i3, i5 = 0, 0, 0
    #     while n > 1:
    #         u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
    #         umin = min((u2, u3, u5))
    #         if umin == u2:
    #             i2 += 1
    #         if umin == u3:
    #             i3 += 1
    #         if umin == u5:
    #             i5 += 1
    #         ugly.append(umin)
    #         n -= 1
    #     return ugly[-1]
    #     """
    #     :type n: int
    #     :rtype: int
    #     """

    def nthUglyNumber(self, n):
        ugly = [1]
        u = [0] * 3
        nums = [2, 3, 5]
        while n > 1:
            temp = [nums[i] * ugly[u[i]] for i in range(3)]
            umin = min(temp)
            while umin in temp:
                index=temp.index(umin)
                u[temp.index(umin)] += 1
                temp[index]=-1
            ugly.append(umin)
            n -= 1
        return ugly[-1]

        """
        :type n: int
        :rtype: int
        """

# Runtime: 36ms
# nums = [1]
#
# i2, i3, i5 = 0, 0, 0
# while len(nums) < 1700:
#     umin = min(2 * nums[i2], 3 * nums[i3], 5 * nums[i5])
#     nums.append(umin)
#     if umin == 2 * nums[i2]: i2 += 1
#     if umin == 3 * nums[i3]: i3 += 1
#     if umin == 5 * nums[i5]: i5 += 1
#
#
# class Solution(object):
#     def nthUglyNumber(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         return nums[n - 1]


solution = Solution()
print(solution.nthUglyNumber(7))

