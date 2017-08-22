# Runtime: 35ms Beats or equals to 91%
# String concatenation is expensive!
class Solution(object):
    def convertToBase7(self, num):
        if num==0:
            return '0'
        elif num<0:
            num*=-1
            negative=True
        else:
            negative=False
        ans,count=0,0
        while num:
            ans+=(num%7)*(10**count)
            num//=7
            count+=1
        return str(-ans) if negative else str(ans)




        """
        :type num: int
        :rtype: str
        """








solution = Solution()
print(solution)

