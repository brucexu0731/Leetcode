# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        

        def dfs(node, maxx):
            nonlocal count 
            if not node:
                return

            if node.val >= maxx:
                maxx = node.val
                count += 1
            
            dfs(node.left, maxx)
            dfs(node.right, maxx)
        
        dfs(root, root.val)

        return count

