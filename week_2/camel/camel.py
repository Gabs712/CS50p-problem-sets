inp = input('camelCase: ')

inp = inp[0].lower() + inp[1:]

for c in inp:
    if c.isupper():
        inp = inp.replace(c, f'_{c.lower()}')
print(inp)
