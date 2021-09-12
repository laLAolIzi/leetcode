class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        stack=[]
        pre=None
        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            if not root.right  or pre==root.right:
                res.append(root.val)
                pre=root
                root=None
            else:
                stack.append(root)
                root=root.right
        return res
