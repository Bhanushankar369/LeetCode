class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        import collections
        dic = collections.Counter(nums)
        heap = []
        for item, freq in dic.items():
            heapq.heappush(heap, [-freq, item])
        ans = []
        for i in range(k):
            bin = heappop(heap)
            ans.append(bin[1])
        return ans
