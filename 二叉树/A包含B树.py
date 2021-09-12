#B是A的子结构
class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B: return False

        def dfs(nodeA):
            if not nodeA: return False
            if nodeA.val == B.val:
                if self.helper(nodeA, B):
                    return True
            return dfs(nodeA.left) or dfs(nodeA.right)

        return dfs(A)

    def helper(self, nodeA, nodeB):
        if not nodeB:
            return True
        if not nodeA or nodeA.val != nodeB.val:
            return False
        return self.helper(nodeA.left, nodeB.left) and self.helper(nodeA.right, nodeB.right)
