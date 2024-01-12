inp = input('Greeting: ')

inp = inp.lower().strip()

if inp.startswith('hello'):
    print('$0')
elif inp.startswith('h'):
    print('$20')
else:
    print('print $100')