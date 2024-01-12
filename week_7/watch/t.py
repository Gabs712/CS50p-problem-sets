import re

x = r'ab\n\''

print(re.search(x, 'ab\n\''))