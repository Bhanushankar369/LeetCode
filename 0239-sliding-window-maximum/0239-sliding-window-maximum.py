class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = deque()
        for ind, val in enumerate(nums):
            while dq and dq[-1] < val:
                dq.pop()
            dq.append(val)

            if ind >= k and nums[ind-k] == dq[0]:
                dq.popleft()

            if ind >= k-1:
                res.append(dq[0])
        return res