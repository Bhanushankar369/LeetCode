class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        lst = defaultdict(list)
        for i in range(len(nums1)):
            lst[nums1[i][0]].append(nums1[i][1])
        for i in range(len(nums2)):
            lst[nums2[i][0]].append(nums2[i][1])
        ans = []
        for key in lst:
            ans.append([key, sum(lst[key])])
        ans = sorted(ans, key=lambda x:x[0])
        return ans