class Solution(object):
    def detectCapitalUse(self, word):
        if not word or len(word)==0:
            return False
        if len(word)==1:
            return True
        if self.isCapital(word[-1]):
            for i in word:
                if not self.isCapital(i):
                    return False
        else:
            for i in range(1,len(word)-1):
                if self.isCapital(word[i]):
                    return False
        return True

        """
        :type word: str
        :rtype: bool
        """
    def isCapital(self,c):
        return ord(c)<91 and ord(c)>64

# print(ord('A'))
# print(ord('Z'))
# print(ord('a'))
# print(ord('z'))

    # Runtime: 35ms
    # def detectCapitalUse(self, word):
    #     """
    #     :type word: str
    #     :rtype: bool
    #     """
    #     if word.istitle():
    #         return True
    #     if word.islower():
    #         return True
    #     if word.isupper():
    #         return True
    #     if word[0].isupper():
    #         if not word[1:].islower():
    #             return False
    #     return False


# Runtime: 45ms Beats or equals to 68%





solution = Solution()
print(solution.detectCapitalUse('FlaG'))

