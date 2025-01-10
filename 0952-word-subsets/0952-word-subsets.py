class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # ans = []
        # x=0
        # single = ''.join(words2)
        # check_dic = collections.Counter(single)
        # print(check_dic)
        # for i in words1:
        #     dic = collections.Counter(i)
        #     x=0
        #     for j in dic:
        #         if j not in check_dic:
        #             continue
        #         elif dic[j] == check_dic[j]:
        #             x+=1
        #     if x==len(check_dic):
        #         ans.append(i)
        # return ans

        counters = [Counter(w) for w in words2]
        max_counter = Counter()
        for c in counters:
            for key, val in c.items():
                max_counter[key] = max(max_counter[key], val)

        res = []
        for word in words1:
            c = Counter(word)
            if max_counter <= c:
                res.append(word)
        return res