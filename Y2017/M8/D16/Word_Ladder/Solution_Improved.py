# Runtime: 135ms Beats or equals to 93%
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        length = 2
        front, back, wordList = set([beginWord]), set([endWord]), set(wordList)
        wordList.discard(beginWord)
        while front:
            front = wordList & (set(
                word[:index] + ch + word[index + 1:] for word in front for index in range(len(beginWord)) for ch in
                'abcdefghijklmnopqrstuvwxyz'))
            if front & back:
                return length
            length += 1
            if len(front) > len(back):
                front, back = back, front
            wordList -= front
        return 0









solution = Solution()
print(solution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))

