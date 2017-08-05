class TwoSum(object):
    #TLEed. Passed 13/16 test cases
    def __init__(self):
        self.store = []
        self.size = 0
        """
        Initialize your data structure here.
        """

    def add(self, number):
        if self.size == 0:
            self.store.append(number)
            self.size += 1
            return
        if number <= self.store[0]:
            self.store.insert(0, number)
        elif number >= self.store[-1]:
            self.store.append(number)
        else:
            lo, hi = 0, self.size - 1
            while True:
                mid = int((lo + hi) // 2)
                if number <= self.store[mid - 1]:
                    hi = mid - 1
                elif number > self.store[mid]:
                    lo = mid + 1
                else:
                    break
            self.store.insert(mid, number)
        self.size += 1

        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """

    def find(self, value):
        if self.size < 2 or value < self.store[0] + self.store[1] or value > self.store[-1] + self.store[-2]:
            return False
        lo, hi = 0, self.size - 1
        while lo < hi:
            temp = self.store[lo] + self.store[hi]
            if temp < value:
                lo += 1
            elif temp > value:
                hi -= 1
            else:
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
obj.add(1)
obj.add(1)
obj.add(3)
obj.add(5)
obj.find(4)
obj.find(7)
