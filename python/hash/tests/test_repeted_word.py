from hash_tables.hash_table import HashTable
import pytest

@pytest.fixture
def hashtable():
    return HashTable()
def test_repeted_word(hashtable):
    str="Once upon a time, there was a brave princess who..."
    actual = hashtable.repeated_word(str)
    expected = 'a'
    assert actual == expected

def test_repeted_word_2(hashtable):
    str="It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."
    actual = hashtable.repeated_word(str)
    expected = 'summer'
    assert actual == expected

def test_repeted_word_3(hashtable):
    str="It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    actual = hashtable.repeated_word(str)
    expected = "it"
    assert actual == expected
    
def test_empty_string(hashtable):
    "test repeated_word"
    assert hashtable.repeated_word('') == ''
