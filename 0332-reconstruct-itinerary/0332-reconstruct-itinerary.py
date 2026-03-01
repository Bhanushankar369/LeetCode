class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)

        ans = []
        
        def dfs(node):
            while graph[node]:
                newNode = graph[node].pop()
                dfs(newNode)
            
            ans.append(node)
        
        dfs("JFK")
        return ans[::-1]