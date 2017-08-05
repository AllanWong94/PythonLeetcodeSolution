class Solution(object):
    def divide(self, dividend, divisor):
        minus=False
        if dividend*divisor<0:
            minus=True
        dividend = abs(dividend)
        divisor = abs(divisor)
        res=0
        if divisor==1:
            if minus:
                res=dividend
            else:
                res=min(dividend,2147483647)

        else:
            while dividend>=divisor:
                dividend-=divisor
                res+=1
        if minus:
            res*=-1
        return res



        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
