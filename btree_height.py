#        1
#       / \
#      /   \
#     2     4
#    / \   / \
#   3   5 6   7
#  / \
# 8   9
#
#

from copy import deepcopy


def find_btree_height(tree):
    if 'left' not in tree and 'right' not in tree:
        return 1

    left_height = right_height = 0

    if 'left' in tree:
        left_height = 1 + find_btree_height(tree['left'])
    if 'right' in tree:
        right_height = 1 + find_btree_height(tree['right'])

    return max(left_height, right_height)


tree1 = {
    'value': 1
}

tree2 = {
    'value': 1,
    'left': {
        'value': 2
    },
    'right': {
        'value': 4
    }
}

tree3 = {
    'value': 1,
    'left': {
        'value': 2,
        'left': {
            'value': 3,
            'left': {
                'value': 8
            },
            'right': {
                'value': 9
            }
        },
        'right': {
            'value': 5
        }
    },
    'right': {
        'value': 4,
        'left': {
            'value': 6,
        },
        'right': {
            'value': 7
        }
    }
}

print(find_btree_height(tree1))
print(find_btree_height(tree2))
print(find_btree_height(tree3))
