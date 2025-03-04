class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        lst=[]
        for i in range(len(mat)):
            lst.append([i, mat[i].count(1)])
        lst.sort(key=lambda x:x[1])
        ans=[]
        for i in range(k):
            ans.append(lst[i][0])
        return ans
        