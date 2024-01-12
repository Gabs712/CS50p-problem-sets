import random as r

while True:
    level = input('Level: ')

    if '-' in level:
        continue
    try:
        level = int(level)
        number = r.randint(1, level)
    except ValueError:
        continue
    break

while True:
    guess = input('Guess: ')

    if '-' in guess:
        continue
    try:
        guess = int(guess)
    except ValueError:
        continue

    if guess < number:
        print('Too small!')
    elif guess > number:
        print('Too large!')
    else:
        print('Just right!')
        break