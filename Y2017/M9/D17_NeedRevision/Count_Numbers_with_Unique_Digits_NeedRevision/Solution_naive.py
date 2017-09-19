class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        count=0
        for i in range(10**n):
            if self.check(i):
                count+=1
        return count
        """
        :type n: int
        :rtype: int
        """
    def check(self,num):
        l=0
        while num:
            temp=1<<(num%10)
            if l&temp:
                return False
            l|=temp
            num//=10
        return True



# Runtime: ms Beats or equals to %





solution = Solution()
print(solution.countNumbersWithUniqueDigits(3))
print(1000-9*9*3-9)
print(solution.countNumbersWithUniqueDigits(9))
print(10000-3*900-3*810)

