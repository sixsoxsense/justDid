import sys

iterable = {"QR": "Qatar Airways", "SQ": "Singapor Airlins"
    , "CX": "Cathay Pacific Airways", "EK": "Emirattes", "KE": "Korean Air Lines"
    , "LH": "Lufthanza German Airlines", "OZ": "Aisiana Airlines"
    , "DL": "Delta Air Lines", "AHC": "Air Hawaii", "QF": "Qantas Airways"}
dict(iterable)


class Node():
    def __init__(self, key, data):
        self.left = None
        self.right = None
        self.key = key
        self.data = data


class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.data = None

    def insert(self, key, data):
        self.root = self._insert_value(self.root, key, data)
        self.data = data
        return self.root is not None

    def _insert_value(self, node, key, data):
        if node is None:
            node = Node(key, data)
        else:
            if key <= node.key:
                node.left = self._insert_value(node.left, key, data)
            else:
                node.right = self._insert_value(node.right, key, data)
        return node

    def in_order_traversal(self):
        def _in_order_traversal(root):
            if root is None:
                pass
            else:
                _in_order_traversal(root.left)
                print(root.key, root.data)
                _in_order_traversal(root.right)

        _in_order_traversal(self.root)

    def __print_helper(self, node, indent, last):
        if node != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(str(node.key))
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    def print_tree(self):
        self.__print_helper(self.root, "", True)


class rbNode():
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1


class RedBlackTree():
    def __init__(self):
        self.TNULL = rbNode(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    def __pre_order_helper(self, node):
        if node != self.TNULL:
            print(node.data + " ")
            self.__pre_order_helper(node.left)
            self.__pre_order_helper(node.right)

    def __in_order_helper(self, node):
        if node != self.TNULL:
            self.__in_order_helper(node.left)
            print(node.data + " ")
            self.__in_order_helper(node.right)

    def __post_order_helper(self, node):
        if node != self.TNULL:
            self.__post_order_helper(node.left)
            self.__post_order_helper(node.right)
            print(node.data + " ")

    def __search_tree_helper(self, node, key):
        if node == self.TNULL or key == node.data:
            return node

        if key < node.data:
            return self.__search_tree_helper(node.left, key)
        return self.__search_tree_helper(node.right, key)

    # Balancing the tree after deletion
    def delete_fix(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0

    def __rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def __delete_node_helper(self, node, key):
        z = self.TNULL
        while node != self.TNULL:
            if node.data == key:
                z = node

            if node.data <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            print
            "Couldn't find key in the tree"
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif (z.right == self.TNULL):
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.delete_fix(x)

    # Balance the tree after insertion
    def fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right

                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def __print_helper(self, node, indent, last):
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.data) + " " + s_color)
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    def preorder(self):
        self.__pre_order_helper(self.root)

    def inorder(self):
        self.__in_order_helper(self.root)

    def postorder(self):
        self.__post_order_helper(self.root)

    def searchTree(self, k):
        return self.__search_tree_helper(self.root, k)

    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def maximum(self, node):
        while node.right != self.TNULL:
            node = node.right
        return node

    def successor(self, x):
        if x.right != self.TNULL:
            return self.minimum(x.right)

        y = x.parent
        while y != self.TNULL and x == y.right:
            x = y
            y = y.parent
        return y

    def predecessor(self, x):
        if (x.left != self.TNULL):
            return self.maximum(x.left)

        y = x.parent
        while y != self.TNULL and x == y.left:
            x = y
            y = y.parent

        return y

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        node = rbNode(key)
        node.parent = None
        node.data = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.data < x.data:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self.fix_insert(node)

    def get_root(self):
        return self.root

    def delete_node(self, data):
        self.__delete_node_helper(self.root, data)

    def print_tree(self):
        self.__print_helper(self.root, "", True)


class DoubleHashing:
    def __init__(self, size):
        self.M = size
        self.a = [None for x in range(size + 1)]
        self.d = [None for x in range(size + 1)]
        self.N = 0

    def hash(self, key):
        return key % self.M

    def put(self, key, data):
        initial_position = self.hash(key)
        i = initial_position
        d = 7 - (key % 7)
        j = 0
        while True:
            if self.a[i] == None:
                self.a[i] = key
                self.d[i] = data
                self.N += 1
            if self.a[i] == key:
                self.d[i] = data
                return
            j += 1
            i = (initial_position + j * d) % self.M
            if self.N > self.M:
                break

    def get(self, key):
        initial_position = self.hash(key)
        i = initial_position
        d = 7 - (key % 7)
        j = 0
        while self.a[i] != None:
            if self.a[i] == key:
                return self.d[i]
            j += 1
            i = (initial_position + j * d) % self.M
        return None

    def print_table(self):
        for i in range(self.M):
            print('{:4}'.format(str(i)), "", end="")
        print()
        for i in range(self.M):
            print('{:4}'.format(str(self.a[i])), "", end="")
        print()


if __name__ == '__main__':
    bst = BinarySearchTree()
    rbt = RedBlackTree()
    print("######이진트리######################")
    for i in iterable.keys():
        bst.insert(i, iterable[i])
    bst.print_tree()
    print("######레드블랙트리#####################")
    for i in iterable.keys():
        rbt.insert(i)
    rbt.print_tree()
    print("######해시코드#######################")
    hashcode = 0
    hashcodeTable = []
    for i in iterable.keys():
        for j in i:
            hashcode = hashcode * 31 + ord(j)
        hashcodeTable.append([hashcode, i])
        hashcode = 0
    print(hashcodeTable)
    print("######이중해싱#######################")
    hashtable = DoubleHashing(15)
    for i in hashcodeTable:
        hashtable.put(i[0], i[1])
    hashtable.print_table()
    print("######txt입력받은뒤 출력################")
    f = open("CARRIERS.txt", encoding="utf-8")
    fileRBT = RedBlackTree()
    reads = f.readlines()
    for read in reads[:5]:
        fileRBT.insert(read[:3])
    fileRBT.print_tree()
    f.close()
