# Runtime: 132ms Beats or equals to 8%
class Solution(object):
    # Reference: https://discuss.leetcode.com/topic/19894/1-11-lines-python-9-lines-c

    def diffWaysToCompute(self, input):
        return [eval(str(a) + c + str(b))
                for i, c in enumerate(input) if c in '+-*'
                for a in self.diffWaysToCompute(input[:i])
                for b in self.diffWaysToCompute(input[i + 1:])] or [int(input)]
        """
        :type input: str
        :rtype: List[int]
        """


    # Runtime: 62ms Beats 32%
    def diffWaysToCompute(self, input):
        return [a+b if c == '+' else a-b if c == '-' else a*b
                for i, c in enumerate(input) if c in '+-*'
                for a in self.diffWaysToCompute(input[:i])
                for b in self.diffWaysToCompute(input[i+1:])] or [int(input)]

# Runtime: 35ms
# class Solution(object):
#     def diffWaysToCompute(self, input):
#         """
#         :type input: str
#         :rtype: List[int]
#         """
#         m = {}
#         return self.helper(input, m)
#
#     def helper(self, input, m):
#         if not input: return []
#         if input.isdigit():
#             return [int(input)]
#         if input in m:
#             return m[input]
#         res = []
#         for i, v in enumerate(input):
#             if v in ('+', '-', '*'):
#                 resB = self.helper(input[0:i], m)
#                 resA = self.helper(input[i + 1:], m)
#                 for b in resB:
#                     for a in resA:
#                         res.append({
#                                        '+': lambda x, y: x + y,
#                                        '-': lambda x, y: x - y,
#                                        '*': lambda x, y: x * y
#                                    }[v](b, a))
#         m[input] = res
#         return res


solution = Solution()
print(solution.diffWaysToCompute('2-1-1'))