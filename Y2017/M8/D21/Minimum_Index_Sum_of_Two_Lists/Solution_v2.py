# Runtime: 102ms Beats or equals to 94% One-time AC.
class Solution(object):
    def findRestaurant(self, list1, list2):
        if len(list1)<len(list2):
            list1,list2=list2,list1
        choice,index_sum,mapRes=None,2000,{}
        for i in range(len(list1)):
            mapRes[list1[i]]=i
        for j in range(len(list2)):
            if list2[j] in mapRes:
                new_sum=j+mapRes[list2[j]]
                if new_sum<index_sum:
                    choice,index_sum=[list2[j]],new_sum
                elif new_sum==index_sum:
                    choice.append(list2[j])
        return choice


        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

