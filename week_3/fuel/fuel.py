while True:
    try:
        x, y = input("Fraction: ").split("/")

        x = int(x)
        y = int(y)

        result = (x / y) * 100
    except (ValueError, ZeroDivisionError):
        continue

    if result > 100:
        continue
    elif result <= 1:
        print("E")
    elif result >= 99:
        print("F")
    else:
        print(f"{result:.0f}%")
    break
