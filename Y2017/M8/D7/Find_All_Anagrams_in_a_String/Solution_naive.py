class Solution(object):
    #TLEed for large s,p. Passed 34/36 test cases.
    def findAnagrams(self, s, p):
        res=[]
        l1,l2=len(s),len(p)
        for i in range(l1-l2):
            dict={}
            for j in range(l2):
                dict[s[i+j]]=dict.get(s[i+j],0)+1
                dict[p[j]]=dict.get(p[j],0)-1
            if self.allZero(dict):
                res.append(i)
        return res

        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        def allZero(dict):
            for i in dict.values():
                if i:return False
            return True