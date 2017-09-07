# Runtime: 835ms Beats or equals to 13%
class Solution(object):
    def combine(self, n, k):
        res=[]
        def helper(n,ptr,num,path):
            if num==0:
                res.append(path)
                return
            if ptr>n:
                return
            helper(n,ptr+1,num-1,path+[ptr])
            helper(n,ptr+1,num,path)
        helper(n,1,k,[])
        return res
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """


# class Solution:
#     def combine(self, n, k):
#         if k == 0:
#             return [[]]
#         return [pre + [i] for i in range(1, n+1) for pre in self.combine(i-1, k-1)]
#
# class Solution:
#     def combine(self, n, k):
#         combs = [[]]
#         for _ in range(k):
#             combs = [[i] + c for c in combs for i in range(1, c[0] if c else n+1)]
#         return combs


solution = Solution()
print(solution.combine(4,2))


