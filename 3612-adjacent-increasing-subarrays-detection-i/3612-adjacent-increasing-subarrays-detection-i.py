from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n < 2 * k:
            return False

        # Compute length of current increasing sequence ending at each index
        inc = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                inc[i] = inc[i-1] + 1

        # Now check if there exist two consecutive increasing subarrays of length k
        for i in range(k - 1, n - k):
            # subarray ending at i has length >= k
            # next subarray of k starts right after i
            if inc[i] >= k and inc[i + k] - inc[i] >= k:
                return True

        # simpler variant using slicing (fixed indices)
        for i in range(n - 2 * k + 1):
            if all(nums[j] < nums[j + 1] for j in range(i, i + k - 1)) and \
               all(nums[j] < nums[j + 1] for j in range(i + k, i + 2 * k - 1)):
                return True
        return False
