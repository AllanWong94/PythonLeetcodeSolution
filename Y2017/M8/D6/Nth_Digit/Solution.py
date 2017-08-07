class Solution(object):
    # Runtime: 32ms Beats or equals to 91%
    def findNthDigit(self, n):
        num = 9
        digit = 1
        while n > num * digit:
            n -= num * digit
            num *= 10
            digit += 1
        base = 10**(digit-1)
        base += (n-1) // digit
        n-=((n-1)//digit)*digit
        return str(base)[n-1]
        print(base)
        print(str(base)[n-1])
        """
        :type n: int
        :rtype: int
        """

    def findNthDigit_Naive(self, n):
        num = 1
        while n > 0:
            l = len(str(num))
            if n > l:
                n -= l
                num += 1
            else:
                print(num)
                return str(num)[n - 1]


obj = Solution()
print(obj.findNthDigit_Naive(45))
print(obj.findNthDigit(45))
