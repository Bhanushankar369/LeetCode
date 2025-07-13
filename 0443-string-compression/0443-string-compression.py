class Solution:
    def compress(self, chars: List[str]) -> int:
        prevChar = chars[0]
        prevVal = 1
        new = []

        for i in range(1, len(chars)):
            if prevChar == chars[i]:
                prevVal += 1
            else:
                new.append(prevChar)
                if prevVal > 1:
                    new += list(str(prevVal))
                prevChar = chars[i]
                prevVal = 1
        new.append(prevChar)
        if prevVal>1:
            new += (list(str(prevVal)))
        print(new)
        for i in range(len(new)):
            chars[i] = new[i]
        return len(new)