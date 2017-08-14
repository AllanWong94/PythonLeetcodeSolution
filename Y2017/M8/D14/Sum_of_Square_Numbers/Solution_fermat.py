# Fermat's Theorem: "Any positive number nn is expressible as a sum of two squares if
#                   and only if the prime factorization of nn, every prime of the form (4k+3)(4k+3)
#                   occurs an even number of times."

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a = 2
        while a * a <= c:
            count = 0
            if c % a == 0:
                while c % a == 0:
                    count += 1
                    c /= a
                if a % 4 == 3 and count % 2 != 0:
                    return False
            a += 1
        return c % 4 != 3
