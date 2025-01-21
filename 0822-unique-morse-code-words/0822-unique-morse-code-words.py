class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans = set()
        s = ""
        for i in range(len(words)):
            s = ""
            for j in words[i]:
                s += morse[ord(j)-97]
            ans.add(s)
        return len(ans)