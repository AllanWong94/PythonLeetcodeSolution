# Runtime: 332ms Beats or equals to 77% One-time AC!
class Solution(object):
    def maxProduct(self, words):
        def charCheck(word):
            res = 0
            for c in word:
                res |= (1 << (ord(c) - 97))
            return res

            # def charCheck(word):
            #     return reduce(lambda x, y: x | y, [1 << (ord(c) - 97) for c in word]) if word else 0

        words.sort(key=len, reverse=True)
        charChecks = [charCheck(word) for word in words]
        l, ans = len(words), 0
        for i in range(l - 1):
            if len(words[i]) * len(words[i + 1]) <= ans:
                return ans
            for j in range(i + 1, l):
                if charChecks[i] & charChecks[j]:
                    continue
                ans = max(ans, len(words[i]) * len(words[j]))
        return ans


# class Solution(object):
#     def maxProduct(self, words):
#         d = {}
#         for w in words:
#             mask = 0
#             for c in set(w):
#                 mask |= (1 << (ord(c) - 97))
#             d[mask] = max(d.get(mask, 0), len(w))
#         return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])


"""
:type words: List[str]
:rtype: int
"""
