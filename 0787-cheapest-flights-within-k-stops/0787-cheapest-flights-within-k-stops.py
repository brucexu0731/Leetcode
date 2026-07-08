from collections import defaultdict, deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for source, dest, price in flights:
            adj[source].append((dest, price))

        queue = deque()
        queue.append((src, 0))
        visit = {}
        visit[src] = 0

        flights = 0
        while queue and flights <= k:
            for i in range(len(queue)):
                curr, price = queue.popleft()
                for nxt, nxt_price in adj[curr]:
                    if (nxt in visit and price + nxt_price < visit[nxt]) or nxt not in visit:
                        visit[nxt] = price + nxt_price
                        queue.append((nxt, price + nxt_price))
            flights += 1
        
        if dst not in visit:
            return -1
        else:
            return visit[dst]
        