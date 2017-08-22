# Runtime: 72ms Beats or equals to 14%
import math

class Solution(object):
    def checkPerfectNumber(self, num):
        if num<2:
            return False
        ans=1
        n=2
        while n*n<num:
            if num%n==0:
                ans+=n+num/n
            n+=1
        if n*n==num:
            ans+=n
        return ans==num

    # Runtime: 36ms
    # Not sure how this works.
    # def checkPerfectNumber(self, num):
    #     """
    #     :type num: int
    #     :rtype: bool
    #     """
    #     if num % 2 == 1 or num <= 0: return False
    #     a = 0
    #     while num % 4 == 0:
    #         num /= 2
    #         a += 1
    #     res = [1]
    #     for j in range(2, 2 + a):
    #         res.append(2 ** j)
    #     for i in range(2, int(math.sqrt(num)) + 1):
    #         if num % i == 0:
    #             res.append(i)
    #             res.append(num / i)
    #     return True if num == sum(res) else False







solution = Solution()
print(solution.checkPerfectNumber(28))

