import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    regex = r'^(?P<x>((\d|1[0-2]):[0-5]\d)|(\d|1[0-2])) (?P<x_fuso>AM|PM) to (?P<y>((\d|1[0-2]):[0-5]\d)|(\d|1[0-2])) (?P<y_fuso>AM|PM)$'
    found = re.search(regex, s)

    if not found:
        raise ValueError

    x, x_fuso, y, y_fuso = found.group('x'), found.group('x_fuso'), found.group('y'), found.group('y_fuso')
    if ':' in x:
        x_h, x_min = x.split(':')
        if 'PM' in x_fuso:
            if x_h == '12':
                x = f'12:{x_min}'
            else:
                x = f'{((int(x_h) + 12) % 24):02}:{x_min}'
        else:
            x = f'{int(x_h) % 12:02}:{x_min}'

    elif not ':' in x:
        if 'PM' in x_fuso:
            if x == '12':
                x = f'12:00'
            else:
                x = f'{((int(x) + 12) % 24):02}:00'
        else:
            x = f'{(int(x) % 12):02}:00'


    if ':' in y:
        y_h, y_min = y.split(':')
        if 'PM' in y_fuso:
            if y_h == '12':
                y = f'12:{y_min}'
            elif y_h != '12':
                y = f'{((int(y_h) + 12) % 24):02}:{y_min}'
        else:
            y = f'{int(y_h):02}:{y_min}'

    elif not ':' in y:
        if 'PM' in y_fuso:
            if y == '12':
                y = f'12:00'
            else:
                y = f'{((int(y) + 12) % 24):02}:00'
        else:
            y = f'{(int(y) % 12):02}:00'


    return f'{x} to {y}'


if __name__ == "__main__":
    main()