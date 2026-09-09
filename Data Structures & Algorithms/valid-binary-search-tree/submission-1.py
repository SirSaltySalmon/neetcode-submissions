# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # we want to use a bounds approach
        # to make sure the relationship is maintained with ancestors
        # further up the tree
        
        def dfs(node, upper_bound, lower_bound):
            if node is None:
                return True

            left_is_correct = (
                node.left is None or
                (node.left.val < node.val and
                node.left.val > lower_bound)
            )

            right_is_correct = (
                node.right is None or
                (node.right.val > node.val and
                node.right.val < upper_bound)
            )
            
            # I go to left of a node? All in left sub tree must be smaller.
            # so upper bound is updated to node val
            # I go to right? All in right sub tree must be bigger
            # so lower bound is updated to node val

            return (
                left_is_correct and right_is_correct and
                dfs(node.left, node.val, lower_bound) and
                dfs(node.right, upper_bound, node.val)
            )
        
        return dfs(root, float("inf"), float("-inf"))