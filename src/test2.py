#
# Binary trees are already defined with this interface:
class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


def minimumDepthBinaryTree(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    if root.left is None:
        return minimumDepthBinaryTree(root.right) + 1

    if root.right is None:
        return minimumDepthBinaryTree(root.left) + 1

    return min(minimumDepthBinaryTree(root.left), minimumDepthBinaryTree(root.right)) + 1


# Driver Program
root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
print(minimumDepthBinaryTree(root))
