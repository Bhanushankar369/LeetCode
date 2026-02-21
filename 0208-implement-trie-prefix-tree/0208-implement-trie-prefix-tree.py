class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfNode = False

class Trie:
    def __init__(self):
        self.head = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.head

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            
            curr = curr.children[c]
        
        curr.isEndOfNode = True

    def search(self, word: str) -> bool:
        curr = self.head

        for c in word:
            if c not in curr.children:
                return False
            else:
                curr = curr.children[c]
        
        return curr.isEndOfNode
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.head

        for c in prefix:
            if c not in curr.children:
                return False
            else:
                curr = curr.children[c]
        
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)