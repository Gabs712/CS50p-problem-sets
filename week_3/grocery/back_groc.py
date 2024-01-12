grocery = {}

while True:
    try:
        item = input().upper()

        if item in grocery:
            grocery[item] = grocery[item] + 1
        else:
            grocery[item] = 1

    except EOFError:
        print()
        sorted_key = sorted(list(grocery))

        for key in sorted_key:
            print(grocery[key], key)
        break
