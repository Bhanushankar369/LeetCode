class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        map = defaultdict(list)
        for u, v in paths:
            map[u].append(v)
        for u,v in paths:
            if v not in map:
                return v
        
        return "Kakinada"