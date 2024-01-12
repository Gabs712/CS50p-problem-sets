from um import count

def test_simpletest():
    assert count('olá, um, bom dia um') == 2

def test_case():
    assert count('UM! olá uM') == 2

def test_middleoftest():
    assert count('dawdumidwja') == 0