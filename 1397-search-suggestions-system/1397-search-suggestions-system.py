class Solution:
    def suggestedProducts(self, arr: List[str], searchWord: str) -> List[List[str]]:
        n = len(arr)

        for i in range(n):
            min_ind = i
            for j in range(i+1, n):
                if arr[j] < arr[min_ind]:
                    min_ind = j

            arr[i], arr[min_ind] = arr[min_ind], arr[i]

        left = 0
        right = n-1

        res = []
        for ind in range(len(searchWord)):
            while left<=right and (len(arr[left]) <= ind or searchWord[ind] != arr[left][ind]):
                left += 1
            while left<=right and (len(arr[right]) <= ind or searchWord[ind] != arr[right][ind]):
                right -= 1
            new = []
            for j in range(min(3, right-left+1)):
                new.append(arr[left+j])
            res.append(new)
        return res
