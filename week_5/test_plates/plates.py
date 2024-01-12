def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[:2].isalpha() and 2 <= len(s) <= 6 and s.isalnum():
        for c in s:
            if c.isdigit():
                index = s.index(c)
                if c != '0' and s[index:].isdigit():
                    return True
                else:
                    return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()