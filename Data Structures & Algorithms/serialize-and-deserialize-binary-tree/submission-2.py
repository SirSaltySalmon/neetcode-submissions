# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# dfs approach
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if node is None:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data_list = data.split(",")
        i = 0

        def dfs():
            nonlocal i
            
            val = data_list[i]
            if val == "N":
                i += 1
                return None
            node = TreeNode(int(val))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()