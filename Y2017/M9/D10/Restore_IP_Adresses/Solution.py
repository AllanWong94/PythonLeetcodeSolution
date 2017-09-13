# Runtime: 48ms Beats or equals to 56%
class Solution(object):
    def restoreIpAddresses(self, s):
        strs = []
        def validNum(_s):
            if _s[0]=='0' and len(_s)>1:
                return False
            if not 0<=int(_s)<256:
                return False
            return True
        def generateS(_s, start, num):
            if num==0:
                if start<len(_s) and validNum(_s[start:]):
                    strs.append(_s)
                return
            for i in range(1,4):
                if start+i>len(_s):
                    return
                pos=start+i
                k=int(_s[start:pos])
                if validNum(_s[start:pos]):
                    generateS(_s[:pos]+'.'+_s[pos:],pos+1,num-1)
                else:
                    break
        generateS(s,0,3)
        return strs

solution = Solution()
print(solution.restoreIpAddresses('25525511135'))








