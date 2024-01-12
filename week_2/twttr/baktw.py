inp = input('Input: ').lower()

for char in inp:
    if char in ['a', 'e', 'i', 'o', 'u']:
        inp = inp.replace(char, '')
print(f'Output: {inp}')