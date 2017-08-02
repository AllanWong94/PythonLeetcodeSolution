
class Solution(object):
    # Runtime: 39ms Beats or equals to 68%
    #Reference: https://discuss.leetcode.com/topic/29845/python-solution
    def isAdditiveNumber(self, num):
        n=len(num)
        for i,j in itertools.combinations(range(1,n), 2):
            a,b=num[:i],num[i:j]
            if num[0]=='0' and len(a)>1:
                return False
            if b!=str(int(b)):
                continue
            while j<n:
                c=str(int(a)+int(b))
                if not num.startswith(c, j):
                    break
                j+=len(c)
                a,b=b,c
            if j==n:
                return True
        return False

        # Runtime: 29ms
        # def isAdditiveNumber(self, num):
        #     """
        #     :type num: str
        #     :rtype: bool
        #     """
        #     for i in range(len(num) - 1):
        #         for j in range(i + 1, len(num)):
        #             n1 = int(num[:i + 1])
        #             n2 = int(num[i + 1:j + 1])
        #             if str(n1) == num[:i + 1] and str(n2) == num[i + 1:j + 1]:
        #                 remain = num[j + 1:]
        #                 sm = str(n1 + n2)
        #                 if len(sm) > len(remain):
        #                     break
        #                 # print n1, n2, remain
        #                 while sm == remain[:len(sm)]:
        #                     n1 = n2
        #                     n2 = int(sm)
        #                     remain = remain[len(sm):]
        #                     sm = str(n1 + n2)
        #                     if len(remain) == 0:
        #                         return True
        #                         # print n1, n2, sm, remain
        #     return False
        """
        :type num: str
        :rtype: bool
        """


solution = Solution()
print(solution.isAdditiveNumber("199100199"))
