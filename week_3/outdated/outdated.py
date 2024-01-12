months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = input('Date: ')

        if '/' in date:
                m, d, y = date.split('/')
                m = int(m)
        elif ' ' in date:
                m, d, y = date.split(' ')

                if not ',' in d:
                      continue
                d = d[:-1]

                if m.capitalize() in months:
                        m = (months.index(m.capitalize()) + 1)
                else:
                    continue
        else:
              continue

        d, y = int(d), int(y)

    except ValueError:
        continue

    if m > 12:
            continue
    elif d > 31:
            continue

    print(f'{y:04}-{m:02}-{d:02}')
    break