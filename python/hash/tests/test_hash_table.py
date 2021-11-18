from hash_tables.hash_table import HashTable
import pytest

@pytest.fixture
def hashtable():
	return HashTable()
'''Adding a key/value to your hashtable results in the value being in the data structure'''
def test_hash_add(hashtable):
    hashtable.add('march 8' , 400)
    expected=400
    actual= hashtable.get('march 8')
    assert actual == expected

"""Successfully returns null for a key that does not exist in the hashtable"""
def test_hash_not_exist(hashtable):
    hashtable.add('march 8' , 400)
    expected=None
    actual= hashtable.get('march 10')
    assert actual == expected


def test_hash(hashtable):
	expected = 700
	actual = hashtable._HashTable__hash("d")
	assert actual == expected

def test_hash_word(hashtable):
	expected = 376
	actual =  hashtable._HashTable__hash("dd")
	assert actual == expected
