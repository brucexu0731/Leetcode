# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        res = -float('inf')

        def dfs(node):
            nonlocal res

            if not node:
                return 0
            
            max_left = dfs(node.left)
            max_right = dfs(node.right)

            res = max(res, node.val + max_left + max_right)

            return max(node.val + max(max_left, max_right), 0)

        dfs(root)

        return res
            
