# Runtime: 642ms Beats or equals to 17%
class Solution(object):
    def reconstructQueue(self, people):
        people.sort(key=lambda x:[x[1],x[0]])
        for i in range(len(people)):
            p=people[i]
            count=0
            for j in range(i):
                if people[j][0]>=p[0]:
                    count+=1
                    if count>p[1]:
                        people.pop(i)
                        people.insert(j,p)
                        break
        return people


        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """







solution = Solution()
print(solution.reconstructQueue([[5,0],[7,0],[6,1],[7,1],[5,2],[4,4]]))

