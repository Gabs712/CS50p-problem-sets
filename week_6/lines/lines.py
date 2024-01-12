import sys

try:
    if len(sys.argv) != 2:
        raise ValueError
    elif not sys.argv[1].endswith('.py'):
        raise ValueError
except ValueError:
    exit('Usage: python lines.py [file].py')

try:
    file = open(sys.argv[1])
except FileNotFoundError:
    sys.exit('File not Found')

linesN = 0
for line in file:
    if line.lstrip(' ').startswith(('#', '\n')):
        continue
    linesN += 1

print(linesN)
file.close