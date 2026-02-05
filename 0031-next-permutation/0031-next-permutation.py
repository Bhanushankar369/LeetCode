class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        dip = -1
        for i in range(len(arr)-2, -1, -1):
            if arr[i] < arr[i+1]:
                dip = i
                break
            
        if dip == -1:
            arr.sort()
            return

        minDiff = float('inf')
        ind = 0

        for j in range(len(arr)-1, dip, -1):
            if arr[j] > arr[dip]:
                arr[j], arr[dip] = arr[dip], arr[j]
                break
        

        arr[dip+1:] = reversed(arr[dip+1:])