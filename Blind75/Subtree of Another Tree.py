class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(root, subRoot):
    
    def sameTree(p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return (sameTree(p.left,q.left) and sameTree(p.right,q.right))
        return False
    
    def dfs(p,q):
        if not q: return True
        if not p: return False
        if sameTree(p,q):
            return True
        return (dfs(p.left,q) or dfs(p.right,q))
    
    return dfs(root,subRoot)
