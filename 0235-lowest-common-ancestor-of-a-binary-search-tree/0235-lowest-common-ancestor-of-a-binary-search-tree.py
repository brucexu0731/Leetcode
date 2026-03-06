# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root 
        while curr:
            l = p.val
            r = q.val
            print(curr.val)
            if (l > curr.val and r < curr.val) or (l < curr.val and r > curr.val):
                return curr
            if l == curr.val or r == curr.val:
                return curr
            
            if l < curr.val and r < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        