import random
from pyfiglet import Figlet, FontNotFound
import sys

figlet = Figlet()

if len(sys.argv) == 1:
    rand = random.choice(figlet.getFonts())
    figlet.setFont(font=rand)

elif sys.argv[1] in ['-f', '--font'] and len(sys.argv) == 3:
    try:
        figlet.setFont(font=sys.argv[2])
    except FontNotFound:
        sys.exit('Invalid usage')

else:
    sys.exit('Invalid usage')

inp = input('Input: ')
print(figlet.renderText(inp))
