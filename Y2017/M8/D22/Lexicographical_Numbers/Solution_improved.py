class Solution(object):
    # Runtime: 1052ms Beats or equals to 59%
    # Reference: https://discuss.leetcode.com/topic/56467/the-most-elegant-python-solution-so-far-10-liner-iterative-o-n-time-o-1-space
    # Each time * 10 for the last element. If larger than n, shrink by 10
    # and increment by 1.
    # If it becomes X0000, start from X.
    def lexicalOrder(self, n):
        ans = [1]
        while len(ans) < n:
            new = ans[-1] * 10
            while new > n:
                new /= 10
                new += 1
                while new % 10 == 0:    # deal with case like 199+1=200 when we need to restart from 2.
                    new /= 10
            ans.append(new)
        return ans