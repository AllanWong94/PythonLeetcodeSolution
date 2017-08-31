# Runtime: 46ms Beats or equals to 83% One-time AC.
class Solution(object):
    # def subsets(self, nums):
    #     res=[]
    #     def helper(index,path):
    #         if index==len(nums):
    #             res.append(path)
    #             return
    #         helper(index+1,path+[nums[index]])
    #         helper(index+1,path)
    #     helper(0,[])
    #     return res

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        result.append([])
        for num in nums:
            next_result = []
            for ls in result:
                ls1 = ls[:]
                ls1.append(num)
                next_result.append(ls1)
            result.extend(next_result)
        return result






solution = Solution()
print(solution.subsets([1,2,3]))

