# Runtime: 122ms Beats or equals to 93%
class Solution(object):
    def findLHS(self, nums):
        if not nums:
            return 0
        dict={}
        for num in nums:
            dict[num]=dict.get(num,0)+1
        ans=0
        for num in dict:
            if num+1 in dict:
                # ans=max(ans,dict[num]+dict[num+1]) Slower!
                if dict[num]+dict[num+1]>ans:
                    ans=dict[num]+dict[num+1]
        return ans