# Runtime: 155ms Beats or equals to 75%
class Solution(object):
    def partition(self, s):
        res=[]
        def helper(str, path):
            if not str:
                res.append(path)
            else:
                helper(str[1:],path+[str[0]])
                for i in range(2,len(str)+1):
                    if str[:i][::-1]==str[:i]:
                        helper(str[i:],path+[str[:i]])
        helper(s,[])
        return res


        """
        :type s: str
        :rtype: List[List[str]]
        """







solution = Solution()
print(solution.partition('bb'))

