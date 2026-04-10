# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        # Questions: can there be negatives? 
    
        # Return a list of node values along every path 
        res = []

        if not root:
            return []

        #DFS to traverse along a path and build up a list, then backtrack and remove each node from the path and go explore another path, if the sum is target push the array into res

        def dfs(path: List[int], node, tot):
            path.append(node.val)
            tot += node.val
            if node.left:
                dfs(path, node.left, tot)
            if node.right:
                dfs(path, node.right, tot)

            if not node.left and not node.right:
                if (tot == targetSum):
                    res.append(path[:])
            
            path.pop()
        
        dfs([], root, 0)

        return res