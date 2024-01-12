import fuel
import pytest

def test_convert():
    with pytest.raises(ValueError):
        fuel.convert('a/a')
    with pytest.raises(ZeroDivisionError):
        fuel.convert('4/0')
    assert fuel.convert('3/4') == 75


def test_gauge():

    assert fuel.gauge(75) == '75%'
    assert fuel.gauge(100) == 'F'
    assert fuel.gauge(1) == 'E'
    assert fuel.gauge(99) == 'Fy'
