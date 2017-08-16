class Solution(object):
    # TLEed.
    def ladderLength(self, beginWord, endWord, wordList):
        open=[[beginWord,0]]
        close,wordList=set(),set(wordList)
        while len(open)>0:
            temp,step=open.pop(0)
            if temp==endWord:
                return step+1
            for word in wordList:
                if word not in close and self.diff(word,temp)==1:
                    open.append([word,step+1])
            close.add(temp)
        return 0

    def diff(self,word1,word2):
        res=0
        for i in range(len(word1)):
            if word1[i]!=word2[i]:
                res+=1
        return res

        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
