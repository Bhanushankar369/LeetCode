class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def dfs(nums):
            if len(nums) == 1:
                return 0 <= abs(nums[0] - 24) < 0.0001
            
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue
                    next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    a, b = nums[i], nums[j]
                    
                    # Try all operations
                    candidates = [a + b, a - b, b - a, a * b]
                    if abs(b) > 1e-6:
                        candidates.append(a / b)
                    if abs(a) > 1e-6:
                        candidates.append(b / a)
                    
                    for val in candidates:
                        if dfs(next_nums + [val]):
                            return True
            return False
        
        return dfs([float(c) for c in cards])
