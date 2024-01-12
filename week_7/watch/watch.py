import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    regex = r'\"https?://(?:www\.)?youtube\.com/embed/([^\"]+)\"'

    if search:= re.search(regex, s):
        return f'https://youtu.be/{search.group(1)}'


if __name__ == "__main__":
    main()