from collections import deque

# last solution was too crazy
# we can just use N as a marker to stop going down that path
class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if node is None:
                result.append("N")
                continue

            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)

        # Remove unnecessary nulls at the end.
        # They do not contain additional structure.
        while result and result[-1] == "N":
            result.pop()

        return ",".join(result)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        values = data.split(",")

        if values[0] == "N":
            return None

        root = TreeNode(int(values[0]))
        queue = deque([root])
        index = 1

        while queue and index < len(values):
            node = queue.popleft()

            # Left child
            if values[index] != "N":
                node.left = TreeNode(int(values[index]))
                queue.append(node.left)
            index += 1

            # Right child
            if index < len(values) and values[index] != "N":
                node.right = TreeNode(int(values[index]))
                queue.append(node.right)
            index += 1

        return root