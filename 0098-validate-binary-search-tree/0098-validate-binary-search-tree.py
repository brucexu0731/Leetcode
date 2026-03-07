# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        isValid = True
        def dfs(node):
            nonlocal isValid
            if not node:
                return [float('-inf'), float('inf')]
            max_left, min_left = dfs(node.left)
            max_right, min_right = dfs(node.right)
            if node.val <= max_left or node.val >= min_right:
                isValid = False
            return [max(node.val, max_right), min(min_left, node.val)]
        
        dfs(root)
        return isValid

        