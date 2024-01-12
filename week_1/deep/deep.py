inp = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

inp = inp.lower().replace('-', ' ').strip()

match inp:
    case '42' | 'forty two':
        print('Yes')
    case _:
        print('No')