from hashlib import md5
import random
import string


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def insert(self, data):
        new_node = ListNode(data)
        current_node = self.head
        self.count += 1

        if not current_node:
            self.head = new_node
            return

        while current_node and current_node.next:
            current_node = current_node.next

        current_node.next = new_node

    def delete(self, value):
        if self.count == 0:
            return False

        if self.head.data == value:
            self.head = self.head.next
            return True

        parent_node = self.head
        current_node = self.head.next

        while current_node and current_node.data != value:
            parent_node = current_node
            current_node = current_node.next

        if not current_node:
            return False

        parent_node.next = parent_node.next.next
        return True

    def at(self, index):
        if index > self.count - 1:
            raise Exception('Index our of range')

        current_node = self.head
        current_index = 0

        while current_node and current_index < index:
            current_node = current_node.next
            current_index += 1

        return current_node

    def __repr__(self):
        values = []
        current_node = self.head

        while current_node:
            values.append(current_node.data)
            current_node = current_node.next

        return f'{values}'


class HashTable:
    def __init__(self, size=1000, debug=False):
        self._table = [None] * size
        self._size = size
        self._debug = debug

    def set(self, key, value):
        hash_index = self._calc_hash_index(key)

        if not isinstance(self._table[hash_index], LinkedList):
            self._table[hash_index] = LinkedList()

        list_of_key_values = self._table[hash_index]
        list_of_key_values.insert((key, value))

        if self._debug:
            print(
                f'hash_index {hash_index} linked list: {repr(list_of_key_values)}')

    def get(self, key):
        hash_index = self._calc_hash_index(key)
        data = self._get_list_data_by_hash_index(key, hash_index)

        return data[1] if data else None

    def delete(self, key):
        hash_index = self._calc_hash_index(key)
        data = self._get_list_data_by_hash_index(key, hash_index)

        if data is None:
            return False

        linked_list_of_key_values = self._table[hash_index]

        return linked_list_of_key_values.delete(data)

    def _get_list_data_by_hash_index(self, key, hash_index):
        linked_list_of_key_values = self._table[hash_index]

        if linked_list_of_key_values is None:
            return None

        current_list_node = linked_list_of_key_values.head

        while current_list_node:
            current_key, _ = current_list_node.data
            if current_key == key:
                return current_list_node.data
            current_list_node = current_list_node.next

        return None

    def _calc_hash_index(self, key):
        return int(md5(key.encode('utf-8')).hexdigest(), 16) % self._size
