class Solution:
    def frequencySort(self, s: str) -> str:
        import collections
        dic = collections.Counter(s)
        import heapq
        heap = []
        for char, freq in dic.items():
            heapq.heappush(heap, [char, freq])
        heap.sort(key=lambda x:-x[1])
        ans = ""
        for ch in heap:
            ans += (ch[0]*ch[1])
        return ans