# Runtime: 545ms Beats or equals to 12%


class Trie(object):

    root=None
    def __init__(self):
        self.root=Node()
        """
        Initialize your data structure here.
        """

    def insert(self, word):
        ptr=self.root
        for c in word:
            if not ptr.next[ord(c)-97]:
                ptr.updateNext(c,Node())
            ptr=ptr.next[ord(c)-97]
        ptr.val=word

        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """

    def search(self, word):
        ptr=self.root
        for c in word:
            ptr=ptr.next[ord(c)-97]
            if not ptr:
                return False
        if ptr.val==word:
            return True
        return False
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

    def startsWith(self, prefix):
        ptr = self.root
        for c in prefix:
            ptr = ptr.next[ord(c) - 97]
            if not ptr:
                return False
        return any(ptr.next) or ptr.val is not None
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

class Node:
    def __init__(self,value=None):
        self.val=value
        self.next=[None]*26

    def updateVal(self,value):
        self.val=value

    def updateNext(self,c,node):
        self.next[ord(c)-97]=node



obj=Trie()
obj.insert('app')
obj.search('app')