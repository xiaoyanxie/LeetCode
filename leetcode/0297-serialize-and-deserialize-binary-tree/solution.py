# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # def sizeOf(node):
        #     maxLevel = 0
        #     stack = [(node, 1)]
        #     while stack:
        #         nxt, level = stack.pop()
        #         if not nxt:
        #             break
        #         maxLevel = max(maxLevel, level)
        #         if nxt.left:
        #             stack.append((nxt.left, level + 1))
        #         if nxt.right:
        #             stack.append((nxt.right, level + 1))
        #     return 2 ** maxLevel - 1

        # arr = list('\u0001' * sizeOf(root))
        # def dfs(node, idx):
        #     if not node:
        #         return
        #     arr[idx] = str(node.val)
        #     if node.left:
        #         dfs(node.left, 2 * idx + 1)
        #     if node.right:
        #         dfs(node.right, 2 * idx + 2)
        
        # dfs(root, 0)
        # return ','.join(arr)

        vals = []
        def dfs(node):
            if not node:
                vals.append('#') # Use '#' as null marker
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        print(vals)
        return ','.join(vals)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        arr = iter(data.split(','))
        def build():
            val = next(arr)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node

        return build()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
