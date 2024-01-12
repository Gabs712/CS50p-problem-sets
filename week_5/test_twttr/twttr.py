def main():
    inp = input('Input: ')
    print(f'Output: {shorten(inp)}')


def shorten(word):
    result = ''
    for c in word:
        if c.lower() not in ['a', 'e', 'i', 'o', 'u']:
            result += c
    return result



if __name__ == "__main__":
    main()