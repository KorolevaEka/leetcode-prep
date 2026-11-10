from solution import clone_json

def test_values():
    value = {'a': [0, None, False, {'x': 'я'}]}
    assert clone_json(value) == value

def test_nested_dictionary_independence():
    value = {'a': {'b': [1]}}
    other = clone_json(value)
    other['a']['b'].append(2)
    assert value == {'a': {'b': [1]}}

def test_root_list_and_nested_list_independence():
    value = [[{'x': 1}], []]
    other = clone_json(value)
    other[0][0]['x'] = 2
    other[1].append(3)
    assert value == [[{'x': 1}], []]

def test_scalars_and_empty_containers():
    for value in (0, False, None, '', [], {}):
        assert clone_json(value) == value
