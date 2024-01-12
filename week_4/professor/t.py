while True:
    try:
        level = int(input('Level: '))
    except ValueError:
        continue

    if level in [1, 2, 3]:
        break
    else:
        print('EEE')