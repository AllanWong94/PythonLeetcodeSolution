# Runtime: 522ms Beats or equals to 16%


class Trie(object):


    def __init__(self):
        self.val=False
        self.next=[None]*26
        """
        Initialize your data structure here.
        """

    def insert(self, word):
        if not word:
            self.val=True
            return
        if not self.next[ord(word[0])-97]:
            self.next[ord(word[0]) - 97]=Trie()
        self.next[ord(word[0])-97].insert(word[1:])

        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """

    def search(self, word):
        if not word:
            return self.val
        if not self.next[ord(word[0])-97]:
            return False
        return self.next[ord(word[0])-97].search(word[1:])
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """

    def startsWith(self, prefix):
        if not prefix:
            return any(self.next) or self.val
        if not self.next[ord(prefix[0]) - 97]:
            return False
        return self.next[ord(prefix[0])-97].startsWith(prefix[1:])
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
