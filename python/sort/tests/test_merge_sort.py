'''Test for code challenge 26'''
from sort.merge_sort import *

def test_reverse_sorted():
    arr = [20,18,12,8,5,-2,-3]
    expected=[-3,-2,5,8,12,18,20]
    actual=mergesort(arr)
    assert actual==expected


def test_few_uniques():
    arr = [5,12,7,5,5,7]
    expected=[5,5,5,7,7,12]
    actual=mergesort(arr)
    assert actual==expected


def test_Nearly_sorted():
    arr =  [2,3,5,7,13,11]
    expected=[2,3,5,7,11,13]
    actual=mergesort(arr)
    assert actual==expected
