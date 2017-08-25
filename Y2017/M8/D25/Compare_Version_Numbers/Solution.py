    # Runtime: 32ms Beats or equals to 94%
class Solution(object):
    def compareVersion(self, version1, version2):
        v1,v2=[int(i) for i in version1.split('.')],[int(i) for i in version2.split('.')]
        while len(v1)>1:
            if v1[-1]:
                break
            else:
                v1.pop(-1)
        while len(v2)>1:
            if v2[-1]:
                break
            else:
                v2.pop(-1)

        for i in range(min(len(v1),len(v2))):
            if v1[i]==v2[i]:
                continue
            if v1[i]>v2[i]:
                return 1
            else:
                return -1
        if len(v1)==len(v2):
            return 0
        if len(v1)>len(v2):
            return 1
        return -1
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """


