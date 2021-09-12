
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        def ino(root):
            if not root:
                return res#[]
            ino(root.left)
            res.append(root.val)
            ino(root.right)
            return res
        return ino(root)