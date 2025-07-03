class Solution:
    def kthCharacter(self, k: int) -> str:
        alice = "a"
        while len(alice) < k:
            for c in alice:
                if c=='z':
                    alice += 'a'
                else:
                    alice += chr(ord(c)+1)
        return alice[k-1]