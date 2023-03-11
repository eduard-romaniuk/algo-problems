class BinaryTree:
    def __init__(self, value: int):
        self.value: int = value
        self.left: BinaryTree = None
        self.right: BinaryTree = None

    def __repr__(self):
        def get_val(node: BinaryTree):
            if node is None:
                return '-'
            return node.value

        return f'n: {self.value} (l: {get_val(self.left)}, r: {get_val(self.right)})'
