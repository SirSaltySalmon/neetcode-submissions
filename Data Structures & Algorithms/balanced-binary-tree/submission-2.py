# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        is_balanced = True

        def dfs(root):
            if root is None:
                return 0
            
            nonlocal is_balanced
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            if abs(left - right) > 1:
                is_balanced = False
            
            return max(left, right) + 1

        dfs(root)
        return is_balanced
