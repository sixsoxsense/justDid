iterable = [["QR", "Qatar Airways"], ["SQ", "Singapor Airlins"]
    , ["CX", "Cathay Pacific Airways"], ["EK", "Emirattes"], ["KE", "Korean Air Lines"]
    , ["LH", "Lufthanza German Airlines"], ["OZ", "Aisiana Airlines"]
    , ["DL", "Delta Air Lines"], ["AHC", "Air Hawaii"], ["QF", "Qantas Airways"]]
dict(iterable)


class Node():
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key=key
        self.data = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_value(self.root, key)
        return self.root is not None

    def _insert_value(self, node, key):
        if node is None:
            node = Node(key)
        else:
            if key <= node.data:
                node.left = self._insert_value(node.left, key)
            else:
                node.right = self._insert_value(node.right, key)
        return node


class redBlackTree():
    pass


if __name__ == '__main__':
    bst=BinarySearchTree()