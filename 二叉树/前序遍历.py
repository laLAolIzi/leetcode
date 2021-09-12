class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []#stack不用加初始化节点，que的话要加
        #if not root: return res#不用加
        while stack or root:
            while root:
                res.append(root.val)
                stack.append(root)#这个和下个换位置就会吧空的root放进去，就不对了
                root = root.left
            root = stack.pop()
            root = root.right
        return res