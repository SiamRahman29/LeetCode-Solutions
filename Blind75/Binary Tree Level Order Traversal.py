# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    result = []
    if not root:
        return  []
    q = [root]

    def bfs(q):
        while True:
            pre = []
            if q == []:
                break
            limit = len(q)
            while limit > 0:
                limit -= 1
                curr = q.pop()
                pre.append(curr.val)
               
                if curr.left:
                    q.insert(0, curr.left)
                    
                if curr.right:
                    q.insert(0, curr.right)
                  
            result.append(pre)

    bfs(q)
    return result