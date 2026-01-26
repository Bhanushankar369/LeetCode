class Solution:
    def subsets(self, arr: List[int]) -> List[List[int]]:
        ans = []

        def sets(ind, ans, temp, arr):
            if ind == len(arr):
                ans.append(temp[:])
                return

            temp.append(arr[ind])
            sets(ind+1, ans, temp, arr)

            temp.pop()
            sets(ind+1, ans, temp, arr)

        sets(0, ans, [], arr)
        return ans