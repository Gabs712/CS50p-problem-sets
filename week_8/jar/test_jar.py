from jar import Jar
from pytest import raises


def test_init():
    jar = Jar(13)
    assert jar.size == 0
    assert jar.capacity == 13


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.cookies == 2
    jar.deposit(3)
    assert jar.size == 5
    with raises(ValueError):
        assert jar.deposit(50)



def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(4)
    assert jar.size == 8
    jar.withdraw(6)
    assert jar.size == 2
    with raises(ValueError):
        assert jar.withdraw(50)