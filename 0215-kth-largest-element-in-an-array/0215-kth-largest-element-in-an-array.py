class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapq.heapify(nums)
        for i in range(k):
            x = heapq.heappop(nums)
        return -x
        