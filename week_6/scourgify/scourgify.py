from sys import argv, exit
import csv

try:
    if len(argv) != 3:
        raise ValueError
    elif not argv[1].endswith('.csv') or not argv[2].endswith('.csv'):
        raise ValueError

except ValueError:
    exit('Usage: scourgify.py [input].csv [output].csv')

students = []
try:
    with open(argv[1]) as input:
        reader = csv.DictReader(input)
        for line in reader:
            last, first = line['name'].replace(' ', '', 1).split(',', 1)
            students.append({'first':first, 'last':last,'house': line['house']})

except FileNotFoundError:
    exit('File not found')

with open(argv[2], 'w') as output:
    writer = csv.DictWriter(output, fieldnames=['first','last', 'house'])
    writer.writeheader()
    for row in students:
        writer.writerow(row)