import random
import string
from hash_table import HashTable


def test_table_collision():
    "Tests the collision"
    obj = HashTable(size=1000)
    random_keys = []

    for i in range(2000):
        random_key = ''.join(random.sample(string.ascii_lowercase, 10))
        random_keys.append(random_key)
        obj.set(random_key, i)

    for i, random_key in enumerate(random_keys):
        assert obj.get(random_key) == i


def test_set_get():
    obj = HashTable(size=1000)
    obj.set('name', 'Ardeshir')

    assert obj.get('name') == 'Ardeshir'


def test_delete():
    obj = HashTable(size=1000)
    obj.set('name', 'Ardeshir')
    obj.delete('name')

    assert obj.get('name') == None

