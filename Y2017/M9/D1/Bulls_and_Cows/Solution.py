import operator
# Runtime: 59ms Beats or equals to 74%

class Solution(object):
    def getHint(self, secret, guess):
        store = {}
        a = b = 0
        for i in secret:
            store[i] = store.get(i, 0) + 1
        for j in range(len(secret)):
            if secret[j] == guess[j]:
                continue
            elif guess[j] in store and store[guess[j]]>0:
                b += 1
                store[guess[j]] -= 1
        return str(a)+'A'+str(b)+'B'

        """
        :type secret: str
        :type guess: str
        :rtype: str
        """





solution = Solution()
print(solution.getHint('1122','1222'))

# Runtime: 36ms
# class Solution(object):
#     def getHint(self, secret, guess):
#         """
#         :type secret: str
#         :type guess: str
#         :rtype: str
#         """
#         bulls = sum(map(operator.eq, secret, guess))
#         both = sum(min(secret.count(x), guess.count(x)) for x in '0123456789')
#         return '%dA%dB' % (bulls, both - bulls)
