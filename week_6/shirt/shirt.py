from sys import argv, exit
from PIL import Image, ImageOps


def main():
    img = validate_inp()
    process_img(img)


def validate_inp():
    try:
        if len(argv) != 3:
            raise ValueError

        if not argv[1].lower().endswith(('.jpg', '.jpeg', '.png')
        ) or not argv[2].lower().endswith(('.jpg','.jpeg', '.png')):
            raise ValueError

        arg1 = argv[1].rsplit('.', 1)
        arg2 = argv[2].rsplit('.', 1)

        if arg1[1].lower() != arg2[1].lower():
            exit('The extensions must be the same')

    except ValueError:
        exit('Usage: shirt.py [input].(jpg, jpeg or png) [output].(jpg, jpeg or png)')

    try:
        return Image.open(arg1[0] + '.' + arg1[1].lower())
    except FileNotFoundError:
        exit('File not found')


def process_img(img):
    shirt = Image.open('shirt.png')
    size = shirt.size

    img = ImageOps.fit(img, size)
    img.paste(shirt, shirt)

    img.save(argv[2])

    img.close()
    shirt.close()


if __name__ == '__main__':
    main()