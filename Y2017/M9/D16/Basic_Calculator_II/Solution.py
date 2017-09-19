# Runtime: 259ms Beats or equals to 51%
# Reference: https://discuss.leetcode.com/topic/16935/share-my-java-solution/3
class Solution(object):
    def calculate(self, s):
        if not s:
            return 0
        cur = 0
        sign = '+'
        stack = []
        for idx, c in enumerate(s):
            if c.isdigit():
                cur = cur * 10 + int(c)
            if c in ('+','-','*','/') or idx==len(s)-1:
                if sign=='+':
                    stack.append(cur)
                elif sign=='-':
                    stack.append(-cur)
                elif sign=='*':
                    stack.append(stack.pop()*cur)
                elif sign=='/':
                    top=stack.pop()
                    if top<0:
                        stack.append(-(abs(top)/cur))
                    else:
                        stack.append(top/cur)
                sign=c
                cur=0
        return sum(stack)
    # Runtime: 115ms
    # def calculate(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     s = s + "+"  # guard
    #     res, num, sign = 0, 0, 1
    #     stack = []
    #     for ss in s:
    #         if ss.isdigit():  # deal with numbers
    #             num = 10 * num + ord(ss) - ord("0")  # faster than int(ss)
    #         elif ss in "+-":
    #             if stack and stack[-1] in "*/":  # update number in a "*/" expression
    #                 md, val = stack.pop(), stack.pop()
    #                 num = val * num if md == "*" else val / num
    #             res, num, sign = res + sign * num, 0, [-1, 1][ss == "+"]
    #         elif ss in "*/":
    #             if stack and stack[-1] in "*/":  # update number in a "*/" expression
    #                 md, val = stack.pop(), stack.pop()
    #                 num = val * num if md == "*" else val / num
    #             stack.extend([num, ss])  # if no previous "*/", append directly
    #             num = 0
    #     return res


solution = Solution()
print(solution.calculate('14-3/2'))
ss='-'
