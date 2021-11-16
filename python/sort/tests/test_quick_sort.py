'''Test for code challenge 28'''
from sort.quick_sort import *

def test_reverse_sorted():
    list = [8,4,23,42,16,15]
    expected=[4,8,15,16,23,42]
    actual=quick_sort(list,0,len(list)-1)
    assert actual==expected


def test_few_uniques():
    list = [5,12,7,5,5,7]
    expected=[5,5,5,7,7,12]
    actual=quick_sort(list,0,len(list)-1)
    assert actual==expected


def test_Nearly_sorted():
    list =  [2,3,5,7,13,11]
    expected=[2,3,5,7,11,13]
    actual=quick_sort(list,0,len(list)-1)
    assert actual==expected
