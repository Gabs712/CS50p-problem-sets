import re
from numb3rs import validate

def test():
    for i in range(256):
        assert validate(f'{i}.0.255.14') == True
    assert validate('0') == False
    assert validate('256.15.25.48') == False
    assert validate('254.48.57') == False
    assert validate('254.48.57.11.') == False
    assert validate('254.48.57') == False
    assert validate('254.48') == False
    assert validate('254.48.') == False
    assert validate('254.5.41.256') == False