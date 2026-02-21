class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfNode = False

class WordDictionary:
    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.head

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.endOfNode = True

    def search(self, word: str) -> bool:
        def dfs(pos, head):
            curr = head

            for i in range(pos, len(word)):
                c = word[i]

                if c == '.':
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                        
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            
            return curr.endOfNode

        return dfs(0, self.head)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)