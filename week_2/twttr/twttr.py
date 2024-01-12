inp = input('Input: ')

for char in inp:
    if char == 'A' or char == 'a':
        inp = inp.replace(char, '')

    elif char == 'E' or char == 'e':
        inp = inp.replace(char, '')

    elif char == 'I' or char == 'i':
        inp = inp.replace(char, '')

    elif char == 'O' or char == 'o':
        inp = inp.replace(char, '')

    elif char == 'U' or char == 'u':
        inp = inp.replace(char, '')
print(f'Output: {inp}')