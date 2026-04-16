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
        queue2 = deque()
        head = Node(node.val, [])

        visit = {node.val: head}
        queue1.append(node)
        queue2.append(head)

        while queue1:
            for i in range(len(queue1)):
                curr1 = queue1.popleft()
                curr2 = queue2.popleft()
                for n1 in curr1.neighbors:
                    if n1.val in visit:
                        curr2.neighbors.append(visit[n1.val])
                        continue 
                    n2 = Node(n1.val, [])
                    curr2.neighbors.append(n2)
                    queue1.append(n1)
                    queue2.append(n2)
                    visit[n1.val] = n2
        
        
        return head
            

        