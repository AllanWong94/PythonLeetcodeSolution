class Solution(object):
    # Runtime:42ms Beats or equals to 27%
    # def canPermutePalindrome(self, s):
    #     map = {}
    #     center = False
    #     for c in s:
    #         if c in map:
    #             map[c] += 1
    #         else:
    #             map[c] = 1
    #     for c in map:
    #         if map[c] % 2 != 0:
    #             if not center:
    #                 center = True
    #                 continue
    #             else:
    #                  return False
    #      return True
    #     """
    #     :type s: str
    #     :rtype: bool
    #     """



    # Runtime: 29ms Beats or equals to 98%
    def canPermutePalindrome(self, s):
        a = set()
        for c in s:
            if c in a:
                a.remove(c)
            else:
                a.add(c)
        return len(a) < 2


solution = Solution()
print(solution.canPermutePalindrome("aab"))
print(solution.canPermutePalindrome("code"))
print(solution.canPermutePalindrome("carerac"))
