from hash_tables.hash_table import HashTable,left_join

def test_joined_left():
    hash1 = HashTable()
    hash1.add('mohammad','silwadi')

    hash2 = HashTable()
    hash2.add('mohammad','momo')

    expected = [['mohammad', 'silwadi', 'momo']]
    actual = left_join(hash1, hash2)

    assert actual == expected
