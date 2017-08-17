# Runtime: 39ms Beats or equals to 43%
class Solution(object):
    def toHex(self, num):
        if num==0:
            return '0'
        if num<0:
            num+=0x100000000
        numbers=[str(i) for i in range(10)]+list('abcdef')
        start,temp=1,1
        while temp*16<=num:
            temp*=16
            start+=1
        res=[0]*(start)
        while num>0:
            res[start-1]=num//temp
            num-=res[start-1]*temp
            temp//=16
            start-=1
        return ''.join([numbers[i] for i in res[::-1]])





solution = Solution()
print(solution.toHex(-1))

