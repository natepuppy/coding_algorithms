def dfs_inorder(root):
    if root:
        dfs_inorder(root.left)
        print(root.val, end=' ')
        dfs_inorder(root.right)

