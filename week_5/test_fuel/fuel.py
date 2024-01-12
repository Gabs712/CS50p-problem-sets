def main():
    while True:
        fraction = input("Fraction: ")

        try:
            print(gauge(convert(fraction)))
            break
        except (ValueError, ZeroDivisionError):
            continue

def convert(fraction):
        x, y = fraction.split('/')

        x = int(x)
        y = int(y)

        return (x / y) * 100

def gauge(percentage):
    if percentage > 100:
        raise ValueError
    elif percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()