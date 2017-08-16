class Solution(object):
    # Runtime: 38ms Beats or equals to 80% Fastest.
    def generatePossibleNextMoves(self, s):
        res=[]
        for i in range(len(s)-1):
            if s[i]=='+' and s[i+1]=='+':
                res.append(s[:i]+'--'+s[min(i+2,len(s)-1):])
        return res


        """
        :type s: str
        :rtype: List[str]
        """
