import re
import sys
import working
import pytest

def test():
    assert working.convert('4 PM to 5 AM') == '16:00 to 05:00'
    assert working.convert('12 AM to 5 AM') == '00:00 to 05:00'
    assert working.convert('2 PM to 5 PM') == '14:00 to 17:00'
    assert working.convert('2:12 PM to 5:42 PM') == '14:12 to 17:42'
    with pytest.raises(ValueError):
        assert working.convert('5 - a')
    with pytest.raises(ValueError):
        assert working.convert('265:00 PM to 489:00 AM')
