class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        import itertools
        map = {'1':"", '2':"abc", '3':"def",
              '4':"ghi",  '5':"jkl",  '6':"mno",  
              '7':"pqrs",  '8':"tuv",  '9':"wxyz"
              }
        if not digits:
            return []
        words = []
        for num in digits:
            words.append(map[num])

        combinations = [''.join(combo) for combo in itertools.product(*words)]

        return combinations 
