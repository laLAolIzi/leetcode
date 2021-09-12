class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recur(l,r):
            if not l and not r:return True
            elif not l or not r or l.val != r.val:return False
            return recur(l.left,r.right) and recur(l.right,r.left)
        return recur(root.left,root.right) if root else True