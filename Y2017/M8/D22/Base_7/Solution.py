# Runtime: 39ms Beats or equals to 59%
class Solution(object):
    def convertToBase7(self, num):
        if num==0:
            return '0'
        elif num<0:
            num*=-1
            negative=True
        else:
            negative=False
        ans=[]
        while num:
            ans.append(str(num%7))
            num//=7
        return '-'+''.join(ans[::-1]) if negative else ''.join(ans[::-1])




        """
        :type num: int
        :rtype: str
        """








solution = Solution()
print(solution)

