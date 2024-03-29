class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root, k):
    result = []
    
    def dfs(root):
        if not root:
            return
        result.append(root.val)
        dfs(root.right)
        dfs(root.left)
    
    dfs(root)
    result.sort()
    
    print(result)
    return result[k-1]
