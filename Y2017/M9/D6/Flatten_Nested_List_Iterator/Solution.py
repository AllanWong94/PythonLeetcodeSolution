# Runtime: 135ms Beats or equals to 35%


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):
    def __init__(self, nestedList):
        def getData(List):
            if List:
                return ([List[0].getInteger()] if List[0].isInteger() else getData(List[0].getList()))+getData(List[1:])
            else:
                return []
        self.storage=getData(nestedList)
        self.ptr,self.l=0,len(self.storage)

        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """



    def next(self):
        if self.hasNext():
            temp=self.storage[self.ptr]
            self.ptr+=1
            return temp
        return None
        """
        :rtype: int
        """

    def hasNext(self):
        return self.ptr<self.l
        """
        :rtype: bool
        """

        # Your NestedIterator object will be instantiated and called as such:
        # i, v = NestedIterator(nestedList), []
        # while i.hasNext(): v.append(i.next())


