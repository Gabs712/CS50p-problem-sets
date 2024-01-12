from bank import value

def test_value():
    assert value('hi') == 20
    assert value('HI') == 20
    assert value('') == 100
    assert value('hello') == 0
    assert value('hi4') == 20
    assert value('0') == 100