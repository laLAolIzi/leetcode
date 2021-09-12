def dfs(root):
    if root == None:
        return

    dfs(root.left)
    dfs(root.right)

def bfs( root) :
    queue=[]
    queue.append(root)
    while queue:
        node = queue.pop(0)
        if node.left != None:
            queue.append(node.left)
        if node.right != None:
            queue.append(node.right)
