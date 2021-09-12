#从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。二维数组形式
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:return []
        res=[]
        que=[root]
        while que:
            tmp=[]
            for _ in range(len(que)):#遍历n次，它值是不会变的
                t=que.pop(0)
                tmp.append(t.val)
                if t.left:que.append(t.left)
                if t.right:que.append(t.right)
            res.append(tmp)
        return res