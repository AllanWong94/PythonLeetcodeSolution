class Solution(object):
    # Runtime: 46ms Beats or equals to 21%
    def isPerfectSquare(self, num):
        base=1
        while (base*2)**2<=num:
            base*=2
        for i in range(base, base*2+1):
            temp=i**2
            if temp<num:
                continue
            elif temp==num:
                return True
            else:
                return False

        """
        :type num: int
        :rtype: bool
        """


#
#
# solution = Solution()
# print(solution.isPerfectSquare(16))

