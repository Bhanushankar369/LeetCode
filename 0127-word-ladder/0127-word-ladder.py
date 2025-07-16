from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        map = defaultdict(list)
        wordList = set(wordList)
        visit = set()

        dq = deque([(beginWord, 1)])
        result = 0

        while dq:
            word, seq = dq.popleft()
            visit.add(word)
            chrList = list(word)

            for ind in range(len(chrList)):
                prev = word[ind]
                for i in range(26):
                    char = chr(i+97)
                    chrList[ind] = char
                    newWord = "".join(chrList)
                    if newWord not in visit and newWord in wordList:
                        if newWord == endWord:
                            return seq+1
                        dq.append((newWord, seq+1))
                chrList[ind] = prev
            
        return 0
