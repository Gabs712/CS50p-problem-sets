from fpdf import *
from PIL import Image


def main():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_margin(0)

    image(pdf)

    top_text(pdf)

    inp = input('Name: ')
    user_text(pdf, inp)

    pdf.output('shirtificate.pdf')


def image(pdf):
    pdf.image('shirtificate.png', 0, 60)


def top_text(pdf):
    topTxt = 'CS50 Shirtificate'

    pdf.set_font('helvetica', size=45)

    txt_width = pdf.get_string_width(topTxt)
    file_width = pdf.w

    center = (file_width - txt_width) / 2

    pdf.text(center, 30, topTxt)


def user_text(pdf, inp):
    inp = f'{inp} took CS50'

    pdf.set_font('helvetica', size=30)
    pdf.set_text_color(255, 255, 255)

    txt_width = pdf.get_string_width(inp)
    file_width = pdf.w

    center = (file_width - txt_width) / 2

    pdf.text(center, 140, inp)


if __name__ == '__main__':
    main()