from binary_tree import BinaryTree


def test_it_is_a_b_tree():
    tree = BinaryTree()
    assert isinstance(tree, BinaryTree)


def test_insert_root():
    tree = BinaryTree()
    tree.insert(5)

    assert tree.get_root().value_of() == 5
    assert isinstance(tree, BinaryTree)

def test_insert_item_bigger_than_root_on_right():
    tree = BinaryTree()
    tree.insert(5)
    tree.insert(10)

    assert tree.get_root().right.value_of() == 10


def test_insert_item_smaller_than_root_on_left():
    tree = BinaryTree()
    tree.insert(5)
    tree.insert(10)
    tree.insert(2)

    assert tree.get_root().left.value_of() == 2


def test_represent_tree():
    tree = BinaryTree()
    tree.insert(5)
    tree.insert(8)
    tree.insert(3)
    tree.insert(1)
    tree.insert(4)
    tree.insert(7)
    tree.insert(9)

    assert repr(tree) == '{"5": {"left": {"3": {"left": {"1": {"left": null, "right": null}}, "right": {"4": {"left": null, "right": null}}}}, "right": {"8": {"left": {"7": {"left": null, "right": null}}, "right": {"9": {"left": null, "right": null}}}}}}'


def test_search_tree_item_found():
    tree = BinaryTree()
    tree.insert(5)
    tree.insert(8)
    tree.insert(3)
    tree.insert(1)
    tree.insert(4)
    tree.insert(7)
    tree.insert(9)

    result_node = tree.find_by_value(4)
    assert result_node.value_of() == 4


def test_search_tree_item_not_found():
    tree = BinaryTree()
    tree.insert(5)
    tree.insert(8)
    tree.insert(3)
    tree.insert(1)
    tree.insert(4)
    tree.insert(7)
    tree.insert(9)

    result_node = tree.find_by_value(20)
    assert result_node == None

