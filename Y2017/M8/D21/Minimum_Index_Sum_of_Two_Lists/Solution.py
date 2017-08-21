# Runtime: 682ms Beats or equals to 12% One-time AC.
class Solution(object):
    def findRestaurant(self, list1, list2):
        choice,index_sum=None,2000
        for i in range(len(list1)):
            if list1[i] in list2:
                new_index_sum=i+self.indexOf(list2,list1[i])
                if new_index_sum<index_sum:
                    choice,index_sum=[list1[i]],i+self.indexOf(list2,list1[i])
                elif new_index_sum==index_sum:
                    choice.append(list1[i])
        return choice


    def indexOf(self,list,restaurant):
        for j in range(len(list)):
            if list[j]==restaurant:
                return j
        return -1
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

