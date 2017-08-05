class TwoSum(object):
    #TLEed. Passed 14/16 test cases
    def __init__(self):
        self.store = []
        self.sums = set()
        self.size = 0
        """
        Initialize your data structure here.
        """

    def add(self, number):
        if self.size > 0:
            for i in self.store:
                self.sums.add(i + number)
        self.store.append(number)
        self.size += 1
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """

    def find(self, value):
        return value in self.sums
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """



        # Your TwoSum object will be instantiated and called as such:
        # obj = TwoSum()
        # obj.add(number)
        # param_2 = obj.find(value)
