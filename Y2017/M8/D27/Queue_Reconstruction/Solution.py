class Solution(object):
    def reconstructQueue(self, people):
        people.sort(key=lambda x:[x[1],x[0]])
        res=[]
        for p in people:
            if not res:
                res.append(p)
            else:
                i=0
                count=0
                while i<len(res) and (p[1]>res[i][1] or (p[1]==res[i][1] and p[0]>res[i][0])):
                    if res[i][0]>=p[0]:
                        count+=1
                        if count>p[1]:
                            break
                    i+=1
                res.insert(i,p)
        return res


        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """



# Runtime: 1022ms Beats or equals to 7% One-time AC!





solution = Solution()
print(solution.reconstructQueue([[5,0],[7,0],[6,1],[7,1],[5,2],[4,4]]))

