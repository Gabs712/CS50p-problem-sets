total = 50
while True:
    if total <= 0:
        print(f'Change Owed: {abs(total)}')
        break

    print(f'Amount Due: {total}')
    inp = int(input('Insert Coin: '))

    if inp != 25 and inp != 10 and inp != 5:
        continue

    elif inp == 25:
            total -= 25
    elif inp == 10:
            total -= 10
    elif inp == 5:
            total -= 5