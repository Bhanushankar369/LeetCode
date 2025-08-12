class TrieNode():
    def __init__(self):
        self.data = ''
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.data = c
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.endOfWord = True

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for word in strs:
            trie.insert(word)

        res = ""
        node = trie.root

        # Keep going while only one child and not end of a word
        while len(node.children) == 1 and not node.endOfWord:
            key = list(node.children.keys())[0]
            res += key
            node = node.children[key]

        return res