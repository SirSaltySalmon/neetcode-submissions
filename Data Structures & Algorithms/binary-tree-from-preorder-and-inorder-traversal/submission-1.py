# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {}
        for i in range(len(inorder)):
            index_map[inorder[i]] = i
        
        def helper(pre_start, pre_finish, in_start, in_finish):
            if pre_start == pre_finish or in_start == in_finish:
                return None
            
            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            index_of_root_in_inorder = index_map[root.val]
            inorder_left_start = in_start
            inorder_left_finish = index_of_root_in_inorder
            inorder_right_start = index_of_root_in_inorder + 1
            inorder_right_finish = in_finish
            
            preorder_left_start = pre_start + 1
            preorder_left_finish = pre_start + 1 + (inorder_left_finish - inorder_left_start)
            preorder_right_start = preorder_left_finish
            preorder_right_finish = pre_finish

            root.left = helper(
                preorder_left_start, preorder_left_finish,
                inorder_left_start, inorder_left_finish
            )
            root.right = helper(
                preorder_right_start, preorder_right_finish, 
                inorder_right_start, inorder_right_finish
            )
            return root
        
        return helper(0, len(preorder), 0, len(inorder))