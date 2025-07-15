class Solution:
    def isValid(self, word: str) -> bool:
        vowel = 'aeiou'
        if len(word) < 3:
            return False

        c, v = False, False
        for i in range(len(word)):
            if not word[i].isalnum():
                return False

            if word[i].lower() in vowel:
                c = True
            
            if word[i].lower() not in vowel and not word[i].isnumeric():
                v = True

        if c and v:
            return True

        return False