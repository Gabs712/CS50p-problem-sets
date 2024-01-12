from plates import is_valid as val

def test():
    assert val('as54') == True
    assert val('asdasdad') == False
    assert val('a 54') == False
    assert val('a50@') == False
    assert val('54asd') == False
    assert val('as54f') == False
    assert val('asd054') == False
    assert val('_asdf') == False
    assert val('as!+_') == False
    assert val('54254') == False
