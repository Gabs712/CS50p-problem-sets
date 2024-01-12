inp = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

inp = inp.lower().replace('-', ' ')

if inp == 'forty two' or inp == '42':
    print('Yes')
else:
    print('No')