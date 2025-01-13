class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        dic = collections.Counter(nums)
        ans = []
        for i in range(max(dic.values())):
            lst = []
            for i in dic:
                if dic[i]>0:
                    lst.append(i)
                    dic[i]-=1
            ans.append(lst)
        return ans