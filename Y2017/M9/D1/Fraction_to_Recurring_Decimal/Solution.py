# Runtime: 29ms Beats or equals to 94%

class Solution(object):
    # Reference: https://discuss.leetcode.com/topic/7876/my-clean-java-solution
    def fractionToDecimal(self, numerator, denominator):
        if numerator==0:
            return '0'
        res=['-'] if (numerator>0) ^ (denominator>0) else ['']
        nume,deno=abs(numerator),abs(denominator)
        res+=[str(nume//deno)]
        nume%=deno
        if nume:
            res.append('.')
        rec={}
        while nume:
            rec[nume]=len(res)
            nume*=10
            res.append(str(nume//deno))
            nume%=deno
            if nume in rec:
                res.insert(rec[nume],'(')
                res.append(')')
                nume=0
            else:
                rec[nume]=len(res)
        return ''.join(res)









solution = Solution()



print(2/7)
print(solution.fractionToDecimal(2,7))
print()


#print(len(str(2/3)))