from calculator import add,sub,multi
def test_add():
    assert add(2,3) == 5
def test_sub():
    assert sub(10,4) == 6
def test_multi():
    assert multi(2,4) == 8