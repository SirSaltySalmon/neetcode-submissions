# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        res = 0

        def dfs(node, largest_so_far: int):
            nonlocal res
            if node is None:
                return
            if node.val >= largest_so_far:
                res += 1
                largest_so_far = node.val
            dfs(node.left, largest_so_far)
            dfs(node.right, largest_so_far)
        
        dfs(root, root.val)
        return res