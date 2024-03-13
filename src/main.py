class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branch_sums(root):
    if root is None:
        return 0

    if root.left is not None:
        if root.left.left is None and root.left.right is None:
            return root.left.value + branch_sums(root.right)

    return branch_sums(root.left) + branch_sums(root.right)

