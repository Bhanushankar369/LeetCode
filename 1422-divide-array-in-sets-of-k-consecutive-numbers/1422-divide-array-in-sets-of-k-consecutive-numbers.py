# import collections
# class Solution:
#     def isPossibleDivide(self, lst: List[int], g_size: int) -> bool:
#         if not lst or len(lst) < g_size:
#             return False
#         count = 0
#         map = collections.Counter(lst)
#         for no in lst:
#             c = False
#             if map[no] > 0:
#                 for j in range(1, g_size):
#                     if no+j in map and map[no+j] > 0:
#                         c = True
#                     else:
#                         c = False
#                         break
#             if c:
#                 for i in range(g_size):
#                     map[no+i] -= 1
#                 count += 1
                
#         for key, val in map.items():
#             if val != 0:
#                 return False
#         return True

import collections
from typing import List

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k != 0:
            return False

        count = collections.Counter(nums)

        for num in sorted(count):
            freq = count[num]
            if freq > 0:
                for i in range(k):
                    if count[num + i] < freq:
                        return False
                    count[num + i] -= freq
        return True
