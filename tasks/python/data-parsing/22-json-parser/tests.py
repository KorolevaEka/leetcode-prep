import pytest
from solution import parse_json as solve

@pytest.mark.parametrize('args, expected', [((' {"a":[1,-2,true,null],"x":"a\\n\\u0410"} ',), {'a': [1, -2, True, None], 'x': 'a\nА'}), (('[]',), []), (('{"a":1,"a":2}',), '!error'), (('[1,]',), '!error'), (('01',), '!error'), (('"\\q"',), '!error'), (('true false',), '!error')])
def test_contract(args, expected):
    if expected == '!error':
        with pytest.raises(ValueError):
            solve(*args)
    else:
        assert solve(*args) == expected

def test_does_not_change_inputs():
    from copy import deepcopy
    args = (' {"a":[1,-2,true,null],"x":"a\\n\\u0410"} ',)
    before = deepcopy(args)
    solve(*args)
    assert args == before


def test_nested_documents_against_json_standard_subset():
    import json
    import random
    rng=random.Random(23)
    def generate(depth):
        if depth==0: return rng.choice([None,True,False,0,-12,'я\n"\\'])
        if rng.randrange(2): return [generate(depth-1) for _ in range(rng.randrange(4))]
        return {str(i):generate(depth-1) for i in range(rng.randrange(4))}
    for _ in range(100):
        expected=generate(3)
        assert solve(json.dumps(expected,ensure_ascii=True))==expected

def test_invalid_tokens_and_boundaries():
    for text in ['', ' ', '+1', '1.', '[1 2]', '{"x" 1}', '{"x":1,}', '"a\nb"', '"\\uD800"', 'falsex']:
        with pytest.raises(ValueError): solve(text)
