import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):    
    if ispunctuation(s) or s.isspace():
        return False
    elif not s[:2].isalpha():
        return False
    elif not 2 <= len(s) <= 6:
        return False
    elif not s.isalpha() and not s[len(s) - 1].isdigit():
        return False
    elif s.isalnum() and start0(s):
        return False
    elif s.isalnum and not sqcdigits(s):
        return False
    else:
        return True


def ispunctuation(s):
    for c in s:
        if c in string.punctuation:
            return True
    return False


def start0(s):
    for c in s:
        if c.isdigit() and c == '0':
            return True
        elif c.isdigit():
            return False
    return False


def sqcdigits(s):
    start = False
    for c in s:
        if c.isdigit() and start == False:
            start = True
        elif not c.isdigit() and start == True:
            return False
    return True

main()
