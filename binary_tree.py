import json


class BinaryTreeSubTreeException(Exception):
    pass


def create_node_repr(node):
    result = {}
    result[node.value_of()] = {
        'left': create_node_repr(node.left) if node.left else None,
        'right': create_node_repr(node.right) if node.right else None
    }

    return result


class TreeNode:
    def __init__(self, value):
        self._value = value
        self.left = None
        self.right = None

    def value_of(self):
        return self._value


class BinaryTree:
    def __init__(self):
        self._root = None

    def insert(self, value):
        if self._root is None:
            self._root = TreeNode(value)
            return True

        if self.find_by_value(value):
            return False

        new_node = TreeNode(value)
        return self._place_new_node(new_node)

    def find_by_value(self, value):
        current_node = self._root
        while current_node:
            if value == current_node.value_of():
                return current_node

            elif value < current_node.value_of():
                current_node = current_node.left
            else:
                current_node = current_node.right

        return current_node

    def __repr__(self):
        if not self._root:
            return '{}'

        return json.dumps(create_node_repr(self._root))

    def get_root(self):
        return self._root

    def _place_new_node(self, new_node):
        current_node = self._root

        while True:
            parent_node = current_node

            if new_node.value_of() > current_node.value_of():
                current_node = current_node.right
                if not current_node:
                    parent_node.right = new_node
                    return True
            else:
                current_node = current_node.left
                if not current_node:
                    parent_node.left = new_node
                    return True
