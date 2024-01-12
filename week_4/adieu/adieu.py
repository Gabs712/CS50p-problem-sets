import inflect

names = list()
en = inflect.engine()

while True:
    try:
        inp = input('Name: ')

    except EOFError:
        print(f'Adieu, adieu, to {en.join(names)}')
        break

    names.append(inp)
