from collections import Counter
class Solution(object):
    def judgeCircle(self, moves):
        c=Counter(moves)
        if (c.get('U')==c.get('D')) and (c.get('L')==c.get('R')):
            return True
        return False

        """
        :type moves: str
        :rtype: bool
        """
    # Runtime: 38ms
    # def judgeCircle(self, moves):
    #     if moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R"):
    #         return True
    #     else:
    #         return False

c=Counter("abcdefe")
print(c.most_common())
print(c.get('a'))




# Runtime: 159ms Beats or equals to 52%





solution = Solution()
print(solution)

