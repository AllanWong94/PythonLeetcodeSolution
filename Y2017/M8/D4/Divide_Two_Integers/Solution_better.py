class Solution(object):
    # Runtime: 55ms Beats or equals to 43%
    # def divide(self, dividend, divisor):
    #     positive = dividend > 0 and divisor > 0
    #     dividend = abs(dividend)
    #     divisor = abs(divisor)
    #     res = 0
    #     while dividend >= divisor:
    #         temp, i = divisor, 1
    #         while dividend >= (temp << 1):
    #             i <<= 1
    #             temp <<= 1
    #         res+=i
    #         dividend-=temp
    #     if positive:
    #         res=min(res, 2147483647)
    #     else:
    #         res*=-1
    #         res=max(res, -2147483648)
    #     return res
    #     """
    #     :type dividend: int
    #     :type divisor: int
    #     :rtype: int
    #     """


    #Runtime: 48ms Beats or equals to 100%
    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)




obj=Solution()
obj.divide(500,3)