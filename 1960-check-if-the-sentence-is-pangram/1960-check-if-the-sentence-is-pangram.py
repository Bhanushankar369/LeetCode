class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha = [0]*26
        for word in sentence:
            alpha[ord(word)-97]+=1
        for i in alpha:
            if i==0:
                return False
        return True