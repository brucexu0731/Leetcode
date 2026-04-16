"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None 

        queue1 = deque()
        head = Node(node.val, [])

        visit = {node.val: head}
        queue1.append(node)

        while queue1:
            for i in range(len(queue1)):
                curr = queue1.popleft()
                for n in curr.neighbors:
                    if n.val in visit:
                        visit[curr.val].neighbors.append(visit[n.val])
                        continue 
                    copy = Node(n.val, [])
                    visit[curr.val].neighbors.append(copy)
                    queue1.append(n)
                    visit[n.val] = copy
        
        
        return head
            

        