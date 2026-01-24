class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergesort(nums, 0, len(nums)-1)
        return nums
        
    def mergesort(self, nums, low, high):
        if low >= high:
            return

        mid = (low+high) // 2
        self.mergesort(nums, low, mid)
        self.mergesort(nums, mid+1, high)

        self.merge(nums, low, mid, high)

    def merge(self, arr, low, mid, high):
        temp = []

        left = low
        right = mid+1

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            
            else:
                temp.append(arr[right])
                right += 1
        
        while left <= mid:
            temp.append(arr[left])
            left += 1
        
        while right <= high:
            temp.append(arr[right])
            right += 1


        for i in range(low, high+1):
            arr[i] = temp[i-low]