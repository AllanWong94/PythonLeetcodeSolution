class Solution(object):
    # Runtime: 2375ms=>1252ms=>1115ms=>975ms Beats or equals to 4%=>51%=>79%=>93%
    # Indexing is expensive!
    def numberOfBoomerangs(self, points):
        res=0
        for p1 in points:
            distances={}
            for p2 in points:
                dist=(p1[0]-p2[0])**2+(p1[1]-p2[1])**2
                distances[dist]=distances.get(dist,0)+1
            for val in distances.values():
                if val>1:
                    res+=val*(val-1)
        return res


        """
        :type points: List[List[int]]
        :rtype: int
        """
