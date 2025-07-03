class Solution:
    def kthCharacter(self, k: int) -> str:
        alice = "a"
        while len(alice) < k:
            temp = ""
            for c in alice:
                if c=='z':
                    temp += 'a'
                else:
                    temp += chr(ord(c)+1)
            alice += temp
        return alice[k-1]