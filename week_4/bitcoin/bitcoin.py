import sys
import requests

def main():
    n = validate_arg()
    dic = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()

    price = dic['bpi']['USD']['rate_float'] * n
    print(f'${price:,.4f}')


def validate_arg():
    try:
        if len(sys.argv) != 2:
            raise ValueError
        return float(sys.argv[1])

    except ValueError:
        sys.exit('Usage: python bitcoin.py [n of bitcoins]')


if __name__ == '__main__':
    main()
