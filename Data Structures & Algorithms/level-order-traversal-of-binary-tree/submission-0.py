# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        res = []
        cur_level = [root]
        while cur_level:
            res_list = []
            nodes = cur_level
            cur_level = []
            for node in nodes:
                res_list.append(node.val)
                if node.left:
                    cur_level.append(node.left)
                if node.right:
                    cur_level.append(node.right)

            res.append(res_list)
        return res
