from seasons import validate, minutes
from pytest import raises
from datetime import date


def test_validate():
    assert validate('2003-07-11') == (2003, 7, 11)