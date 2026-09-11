# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")

        def dfs(node):
            if node is None:
                return 0

            nonlocal res

            sum_left = dfs(node.left)
            sum_right = dfs(node.right)

            total = node.val
            if sum_left > 0:
                total += sum_left
            if sum_right > 0:
                total += sum_right
            
            res = max(res, total)
            return node.val + max(0, sum_left, sum_right)
        
        dfs(root)
        return res