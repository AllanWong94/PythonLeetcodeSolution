import sys
class TwoSum(object):
    # Runtime:126ms Beats 100%
    # Rule out all cases that are too small or too big inputs for finds.
    # Better judgement (1 less than previous)
    def __init__(self):
        self.dict={}
        self.minNum=sys.maxint
        self.maxNum=-sys.maxint
        """
        Initialize your data structure here.
        """

    def add(self, number):
        self.dict[number]=self.dict.get[number,0]+1
        self.minNum=min(self.minNum,number)
        self.maxNum=max(self.maxNum,number)


        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """

    def find(self, value):
        if value<2*self.minNum or value>2*self.maxNum:
            return False
        return any(value-num in self.dict and (value-num!=num or self.dict[num]>1) for num in self.dict.keys())
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """



        # Your TwoSum object will be instantiated and called as such:
        # obj = TwoSum()
        # obj.add(number)
        # param_2 = obj.find(value)