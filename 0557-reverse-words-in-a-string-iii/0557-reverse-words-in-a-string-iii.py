class Solution:
    def reverseWords(self, s: str) -> str:
        sentence = ""
        lst = s.split()
        for i in lst:
            sentence += i[::-1]
            sentence += " "
        return sentence[:len(sentence)-1]