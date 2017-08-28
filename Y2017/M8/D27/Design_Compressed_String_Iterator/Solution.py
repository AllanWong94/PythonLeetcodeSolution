# Runtime: 88ms=>72ms=>62ms Beats or equals to 20%=>56%=>88%
# type casting is expensive!
class StringIterator(object):
    def __init__(self, compressedString):
        self.str = compressedString
        self.ptr = 0
        self.count=0
        """
        :type compressedString: str
        """

    def next(self):
        if not self.hasNext():
            return ' '
        if self.count==0:
            str=self.str
            self.c=str[self.ptr]
            self.ptr+=1
            start=self.ptr
            while self.ptr<len(str) and str[self.ptr].isdigit():
                self.count = self.count * 10 + ord(self.str[self.i]) - ord("0")
                self.ptr+=1
            # self.count=int(str[start:self.ptr])
        self.count-=1
        return self.c

    def hasNext(self):
        return self.count>0 or self.ptr < len(self.str)
        """
        :rtype: bool
        """

    def handle(self, abbr):
        res = []
        num = ptr = 0
        while ptr < len(abbr):
            try:
                temp = int(abbr[ptr])
                num = num * 10 + temp
            except:
                if num > 0:
                    res.append(num)
                    num = 0
                res.append(abbr[ptr])
            ptr += 1
        if num > 0:
            res.append(num)
        return res



        # Your StringIterator object will be instantiated and called as such:


obj = StringIterator("L1e2t1C1o1d1e11")
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())

# param_1 = obj.next()
# param_2 = obj.hasNext()


