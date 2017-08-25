# Runtime: 36ms Beats or equals to 74%
class Solution(object):
    def checkRecord(self, s):
        count0=count1=0
        late=False
        for i in s:
            if i=='L':
                count0+=1
                if count0>2:
                    return False
            else:
                count0=0
                if i=='A':
                    count1+=1
                    if count1>1:
                        return False
        return True


        # Runtime: 32ms
        # def checkRecord(self, s):
        #     """
        #     :type s: str
        #     :rtype: bool
        #     """
        #     return True if s.count('A') < 2 and s.find('LLL') < 0 else False


        """
        :type s: str
        :rtype: bool
        """








solution = Solution()
print(solution)

