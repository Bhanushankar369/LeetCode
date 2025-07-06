class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = set()
        def dfs(room):
            visit.add(room)
            for nei in rooms[room]:
                if nei not in visit:
                    dfs(nei)
        dfs(0)
        return len(visit) == len(rooms)