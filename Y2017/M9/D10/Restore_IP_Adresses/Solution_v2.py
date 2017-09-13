# Runtime: 45ms Beats or equals to 67%
class Solution(object):
    def restoreIpAddresses(self, s):
        strs=[]
        def helper(_s, k, temp):
            if len(_s)>3*k:
                return
            if k==0:
                strs.append(temp[:])
                return
            for i in range(min(3,len(_s)-k+1)):
                if (i==2 and int(_s[:3])>255) or (i>0 and _s[0]=='0'):
                    continue
                helper(_s[i+1:],k-1,temp+[_s[:i+1]])
        helper(s,4,[])
        return ['.'.join(x) for x in strs]


        """
        :type s: str
        :rtype: List[str]
        """

# Runtime: 39ms
# class Solution(object):
#     def restoreIpAddresses(self, s):
#         """
#         :type s: str
#         :rtype: List[str]
#         """
#         ans = []
#         self.helper(ans, s, 4, [])
#         return ['.'.join(x) for x in ans]
#
#     def helper(self, ans, s, k, temp):
#         if len(s) > k * 3:
#             return
#         if k == 0:
#             ans.append(temp[:])
#         else:
#             for i in range(min(3, len(s) - k + 1)):
#                 if i == 2 and int(s[:3]) > 255 or i > 0 and s[0] == '0':
#                     continue
#                 self.helper(ans, s[i + 1:], k - 1, temp + [s[:i + 1]])