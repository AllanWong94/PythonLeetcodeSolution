# Runtime: 42ms Beats or equals to 83% Fastest.
# Edge cases must be taken into consideration! e.g final letter is a number.
class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        ptr=0
        start=-1
        for i in range(len(abbr)):
            if abbr[i].isdigit():
                if start==-1:
                    if abbr[i]=='0':
                        return False
                    start=i
            else:
                if start!=-1:
                    ptr+=int(abbr[start:i])
                    start=-1
                if ptr>=len(word) or abbr[i]!=word[ptr]:
                    return False
                ptr+=1
        if start!=-1:
            ptr+=int(abbr[start:])
        if ptr!=len(word):
                return False
        return True



        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """

    def handle(self,abbr):
        res=[]
        num=ptr=0
        while ptr<len(abbr):
            try:
                temp=int(abbr[ptr])
                num=num*10+temp
            except:
                if num>0:
                    res.append(num)
                    num=0
                res.append(abbr[ptr])
            ptr+=1
        if num>0:
            res.append(num)
        return res






solution = Solution()
print(solution.handle('i12iz4n'))
print(solution.validWordAbbreviation('internationalization','i12iz4n'))
print(solution.validWordAbbreviation('a','2'))
print(solution.validWordAbbreviation('internationalization','i5a11o1'))

