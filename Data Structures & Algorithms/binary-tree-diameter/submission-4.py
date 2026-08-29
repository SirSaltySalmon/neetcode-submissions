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
    diameter_hash = {}

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depth_hash = {}
        self.diameter_hash = {}
        self.depthOfTree(root)
        return max(self.diameter_hash.values())
    
    def depthOfTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        depth_left = self.depthOfTree(root.left)
        depth_right = self.depthOfTree(root.right)
        depth = 0
        if root not in self.depth_hash:
            depth = max(depth_left, depth_right) + 1
            self.depth_hash[root] = depth
        else:
            depth = self.depth_hash[root]
        
        diameter = 0
        if root not in self.diameter_hash:
            diameter = depth_left + depth_right
            self.diameter_hash[root] = diameter
        else:
            diameter = self.diameter_hash[root]
        
        return depth