# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# diameter is depth of left subtree + depth of right subtree
# to do that right, must return:
# diameter AND depth so parent tree can
# max(depths, diameter left, diameter right)
class Solution:
    depth_hash = {}

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth_left = self.depthOfTree(root.left)
        depth_right = self.depthOfTree(root.right)
        diameter = depth_left + depth_right
        return max(
            diameter,
            self.diameterOfBinaryTree(root.left),
            self.diameterOfBinaryTree(root.right)
        )
    
    def depthOfTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = self.depth_hash.get(root,
            max(
                self.depthOfTree(root.left),
                self.depthOfTree(root.right)
                ) + 1
        )
        self.depth_hash[root] = depth
        return depth
        