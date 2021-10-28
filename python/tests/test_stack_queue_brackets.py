from stack_and_queue.stack_queue_brackets import validate_brackets

def test_balanced_one():
    excepted = 'TRUE'
    actual = validate_brackets('{{()}}')
    assert excepted == actual

def test_validate_brackets_tow():
    excepted = 'TRUE'
    actual = validate_brackets('{([])}')
    assert excepted == actual

def test_not_validate_brackets_one():
    excepted = 'FALSE'
    actual = validate_brackets('{})')
    assert excepted == actual

def test_not_validate_brackets_tow():
    excepted = 'FALSE'
    actual = validate_brackets('{[()])')
    assert excepted == actual
