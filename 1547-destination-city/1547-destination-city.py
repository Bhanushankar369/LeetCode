class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        map = defaultdict(list)
        visit = set()
        for u, v in paths:
            map[u].append(v)
            visit.add(u)
            visit.add(v)
        for item in visit:
            if len(map[item]) == 0:
                return item
        
        return "Kakinada"