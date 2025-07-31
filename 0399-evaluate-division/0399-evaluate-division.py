val = 10**8
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        elements = []
        for u, v in equations:
            if u not in elements:
                elements.append(u)
            if v not in elements:
                elements.append(v)
        
        index_map = {var: idx for idx, var in enumerate(elements)}

        map = defaultdict(float)
        ind = 0
        for u, v in equations:
            map[(u, v)] = values[ind]
            ind+=1

        n = len(elements)
        dist = [[val for _ in range(n)] for _ in range(n)]
        for x in range(n):
            for y in range(n):
                if x == y:
                    dist[x][y] = 1
                if (elements[x], elements[y]) in map:
                    dist[x][y] = map[(elements[x], elements[y])]
                    dist[y][x] = 1/(map[(elements[x], elements[y])]) 

        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][via] != val and dist[via][j] != val:
                        if dist[i][j] == val:
                            dist[i][j] = dist[i][via] * dist[via][j]

        result = []
        for u, v in queries:
            if u in index_map and v in index_map and dist[index_map[u]][index_map[v]] != val:
                result.append(dist[index_map[u]][index_map[v]])
            else:
                result.append(-1.0)

        return result