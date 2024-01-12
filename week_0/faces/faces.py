def main():
    inp = input("Include: :) or :(\n")
    convert(inp)


def convert(emoti):
    emoti = emoti.replace(':)', '🙂').replace(':(', '🙁')
    print(emoti)


main()
