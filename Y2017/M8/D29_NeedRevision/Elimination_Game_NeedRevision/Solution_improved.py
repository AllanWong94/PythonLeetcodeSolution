class Solution(object):
    # Runtime: 99ms Beats or equals to 40%
    # def lastRemaining(self, n):
    #     head = step = 1
    #     length = n
    #     left = True
    #     while length > 1:
    #         if left or length % 2 == 1:
    #             head += step
    #         length //= 2
    #         step *= 2
    #         left = not left
    #     return head
    #
    #     """
    #     :type n: int
    #     :rtype: int
    #     """

    def lastRemaining(self,n):
        return 1 if n==1 else 2*(1+n//2-self.lastRemaining(n//2))



    # Runtime: ms Beats or equals to %





solution = Solution()
print(solution.lastRemaining(9))
