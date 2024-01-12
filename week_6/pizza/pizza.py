import sys
import tabulate
import csv

try:
    if len(sys.argv) != 2:
        raise ValueError
    elif not sys.argv[1].endswith('.csv'):
        raise ValueError
    file = open(sys.argv[1])
except ValueError:
    exit('Usage: python pizza.py [file].csv')
except FileNotFoundError:
    exit('File not Found')

items= []
reader = csv.reader(file)

for row in reader:
    items.append(row)

file.close()

print(tabulate.tabulate(items[1:], headers=items[0], tablefmt='rounded_grid'))
