class TwoSum(object):
    # Reference: https://discuss.leetcode.com/topic/6379/my-solutions-in-java-c-and-python-o-1-time-for-add-o-n-time-for-find-o-n-space
    # Runtime:835ms Beats 11%
    def __init__(self):
        self.store = {}
        self.size=0
        """
        Initialize your data structure here.
        """

    def add(self, number):
        self.store[number] = self.store.get(number, 0) + 1
        self.size+=1
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """

    def find(self, value):
        if self.size < 2:
            return False
        for i in self.store.keys():
            j = value - i
            if j == i and self.store.get(i) > 1 or j != i and self.store.get(j, 0) > 0:
                return True
        return False

        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """



        # Your TwoSum object will be instantiated and called as such:
        # obj = TwoSum()
        # obj.add(number)
        # param_2 = obj.find(value)


obj = TwoSum()
obj.add(0)
obj.add(-1)
obj.add(1)
obj.find(0)

