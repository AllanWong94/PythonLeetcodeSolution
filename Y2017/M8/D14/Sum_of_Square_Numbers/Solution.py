# Runtime: 489ms Beats or equals to 9%
class Solution(object):
    def judgeSquareSum(self, c):
        i = 0
        squares = set()
        while i ** 2 <= c:
            squares.add(i ** 2)
            i += 1

        for i in squares:
            if c - i in squares:
                return True

        return False

        """
        :type c: int
        :rtype: bool
        """








solution = Solution()
print(solution)

