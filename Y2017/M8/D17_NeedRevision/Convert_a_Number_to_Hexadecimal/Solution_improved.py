# Runtime: 35ms Beats or equals to 60% Fastest
class Solution(object):
    def toHex(self, num):
        res=[]
        if num<0:
            num+=0x100000000
        numbers='0123456789abcdef'
        while num:
            res.append(numbers[num%16])
            num//=16
        return ''.join(res[::-1]) if res else '0'





solution = Solution()
print(solution.toHex(-1))

