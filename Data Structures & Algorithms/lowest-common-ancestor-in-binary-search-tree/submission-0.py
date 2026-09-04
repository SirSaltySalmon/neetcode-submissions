# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = root

        def dfs(node):
            nonlocal res

            if node is None:
                return False

            left = dfs(node.left)
            right = dfs(node.right)
            self_descent = node.val == p.val or node.val == q.val
            if res == root:
                if (self_descent and (left or right)) or (left and right):
                    res = node
            
            return left or right or self_descent
        
        dfs(root)
        return res

