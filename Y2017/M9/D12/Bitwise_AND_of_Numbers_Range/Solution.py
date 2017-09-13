# Runtime: 108ms Beats or equals to 75%

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        if m == n:
            return m
        def log2(k):
            count=-1
            while k:
                k>>=1
                count+=1
            return count
        lo, hi = log2(m), log2(n)
        if lo != hi:
            return 0
        gap = n - m
        start = log2(gap) + 1
        res = 1 << lo
        for i in range(start, lo):
            # print(i)
            # print(m & ((1 << i) - 1))
            # print((m & (1 << i - 1)) + gap)
            # print(1 << i)
            # print((m >> i) & 1)
            if ((m >> i) & 1) and ((1 << i) > ((m & ((1 << i) - 1)) + gap)):
                res |= 1 << i
        return res
        """
        :type m: int
        :type n: int
        :rtype: int
        """
    # Runtime: 92ms
    # def rangeBitwiseAnd(self, m, n):
    #     while m<n:
    #         n&=n-1
    #     return n



print(bin(21))
solution = Solution()
print(bin(solution.rangeBitwiseAnd(21,24)))

for i in range(21,25):
    print(bin(i))



