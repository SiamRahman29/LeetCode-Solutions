class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def serialize(root):
    """Encodes a tree to a single string.
    
    :type root: TreeNode
    :rtype: str
    """
    res = []

    def dfs(node):
        if not node:
            res.append("N")
            return
        res.append(str(node.val))
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    return ",".join(res)

def deserialize(data):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
    vals = data.split(",")
    i = 0

    def dfs():
        if vals[i] == "N":
            i += 1
            return None
        node = TreeNode(int(vals[i]))
        i += 1
        node.left = dfs()
        node.right = dfs()
        return node
    return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deserialize(serialize(root))
