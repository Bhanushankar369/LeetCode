import re
from collections import Counter

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        banned_set = set(banned)
        words = re.findall(r'\w+', paragraph.lower())
        counter = Counter(words)
        for word, _ in counter.most_common():
            if word not in banned_set:
                return word