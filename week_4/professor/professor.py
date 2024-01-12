import random as r


def main():
    score = 0
    level = get_level()
    for _ in range(10):

        x = generate_integer(level)
        y = generate_integer(level)

        for trie in range(3):
            try:
                answ = int(input(f'{x} + {y} = '))

                if x + y != answ:
                    raise ValueError
                else:
                    score += 1
                    break

            except ValueError:
                print('EEE')

                if trie == 2:
                    print(f'{x} + {y} = {x + y}')
                continue

    print(f'Score: {score}')


def get_level():
    while True:
        try:
            inp = int(input('Level: '))
            if inp in [1, 2, 3]:
                return inp

        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return r.randint(0, 9)
    elif level == 2:
        return r.randint(10, 99)
    elif level == 3:
        return r.randint(100, 999)


if __name__ == "__main__":
    main()