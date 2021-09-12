class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        stack=[]
        while root or stack:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            res.append(root.val)
            root=root.right
        return res
#三件套while while:append root 出来root=pop