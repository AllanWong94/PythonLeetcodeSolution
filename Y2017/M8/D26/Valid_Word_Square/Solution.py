# Runtime: 75ms Beats or equals to 74%
class Solution(object):
    def validWordSquare(self, words):
        n=len(words)
        up=down=0
        for i in range(n):
            down+=min(i,len(words[i]))
            up+=max(len(words[i]),i+1)-i-1
        if up!=down:
            return False
        for i in range(n):
            for j in range(i+1,len(words[i])):
                if j>=n or i>=len(words[j]) or words[i][j]!=words[j][i]:
                    return False
        return True


        """
        :type words: List[str]
        :rtype: bool
        """




    # Runtime: 42ms
    # def validWordSquare(self, words):
    #     t = map(None, *words)
    #     return t == map(None, *t)





test=['abcd','ef']
t=map(None,*test)
print(t[0])


solution = Solution()
print(solution)

