class Solution(object):
    # Runtime: 203ms Beats or equals to 72%
    def findAnagrams(self, s, p):
        res = []
        l1, l2 = len(s), len(p)
        if l1 < l2:
            return res
        dict1, dict2 = [0] * 123, [0] * 123
        for c in p:
            dict1[ord(c)] += 1
        for c in s[:l2]:
            dict2[ord(c)] += 1
        if dict1 == dict2: res.append(0)
        for i in range(l2):
            dict2[ord(s[i + l2])] += 1
            dict2[ord(s[i])] -= 1
            if dict1==dict2: res.append(i)
        return res

solution = Solution()
print(solution.findAnagrams("abab", "ab"))
print(solution.findAnagrams("cbaebabacd", "abc"))
