# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        all_nodes = []
        all_nodes += self.inorderTraversal(root.left)
        all_nodes += [root.val]
        all_nodes += self.inorderTraversal(root.right)
        return all_nodes