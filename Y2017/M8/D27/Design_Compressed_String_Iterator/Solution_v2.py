class StringIterator(object):
    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.i = 0
        self.count = 0
        self.c = None
        self.str = compressedString

    def next(self):
        """
        :rtype: str
        """
        if self.hasNext() is False:
            return " "
        if self.count == 0:
            self.c = self.str[self.i]  # get character
            self.count = 0  # how many characters
            self.i += 1  # move to next index
            # calculate total number of characteris
            while self.i < len(self.str) and ord(self.str[self.i]) <= ord('9') and ord(self.str[self.i]) >= ord('0'):
                self.count = self.count * 10 + ord(self.str[self.i]) - ord("0")
                self.i = self.i + 1

        self.count -= 1
        return self.c

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.count > 0 or self.i < len(self.str)
