# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if root is None:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            if left is False or right is False:
                return False
            
            if abs(left - right) > 1:
                return False
            
            return max(left, right) + 1

        return dfs(root) is not False
        