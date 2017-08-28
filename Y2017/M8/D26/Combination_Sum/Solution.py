class Solution(object):
    def combinationSum(self, candidates, target):
        candidates.sort()
        res=[]
        def helper(target, index, path):
            if target==0:
                res.append(path)
                return
            for i in range(index,len(candidates)):
                if target>=candidates[i]:
                    helper(target-candidates[i],i,path+[candidates[i]])
        helper(target,0,[])
        return res




        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
# Runtime: 162ms=>152ms=>148ms=>105ms=>78ms Beats or equals to 33%=>43%=>48%=>70%=>95%
# Reference: https://discuss.leetcode.com/topic/23142/python-dfs-solution
# local functions => faster
# less params => faster
# indexing costs.