class Solution(object):
    # DP.
    # Reference: https://discuss.leetcode.com/topic/23893/my-expressive-python-solution/2
    def nthUglyNumber(self, n):
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            umin = min((u2, u3, u5))
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly.append(umin)
            n -= 1
        return ugly[-1]
        """
        :type n: int
        :rtype: int
        """



# Runtime: ms Beats or equals to %





solution = Solution()
print(solution.nthUglyNumber(10))

