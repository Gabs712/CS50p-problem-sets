import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    regex = r'\bum\b'
    ums = re.findall(regex, s, re.IGNORECASE)

    count = 0
    for um in ums:
        count += 1
    return count


if __name__ == "__main__":
    main()