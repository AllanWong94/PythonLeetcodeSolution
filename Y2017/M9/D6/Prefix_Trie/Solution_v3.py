# Runtime: 212ms Beats or equals to 95%
class Trie(object):
    def __init__(self):
        self.data={}

        """
        Initialize your data structure here.
        """

    def insert(self, word):
        ptr=self.data
        for w in word:
            if w not in ptr:
                ptr[w]={}
            ptr=ptr[w]
        if '?' not in ptr:
            ptr['?']=True
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """

    def search(self, word):
        ptr=self.data
        for w in word:
            if w not in ptr:
                return False
            ptr=ptr[w]
        return '?' in ptr
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

    def startsWith(self, prefix):
        ptr = self.data
        for w in prefix:
            if w not in ptr:
                return False
            ptr = ptr[w]
        return len(ptr)>0
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """



        # Your Trie object will be instantiated and called as such:
        # obj = Trie()
        # obj.insert(word)
        # param_2 = obj.search(word)
        # param_3 = obj.startsWith(prefix)