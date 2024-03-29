class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if not root:
        return None

    temp = root.right
    root.right = root.left
    root.left = temp
    invertTree(root.left)
    invertTree(root.right)
    return root
