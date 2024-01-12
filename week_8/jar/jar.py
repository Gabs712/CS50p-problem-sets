class Jar:

    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError('Negative number is not allowed')

        self._capacity = capacity
        self.cookies = 0

    def __str__(self):
        return '🍪' * self.cookies

    def deposit(self, n):
        self.cookies += n
        if self.cookies > self._capacity:
            raise ValueError('The jar is full')

    def withdraw(self, n):
        self.cookies -= n
        if self.cookies < 0:
            raise ValueError('The jar is already empty')

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies


x = Jar()

print(x)