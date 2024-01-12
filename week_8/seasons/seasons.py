from datetime import date, datetime
from re import search
from inflect import engine
from sys import exit



def main():
    birth = validate(input('Date of birth: '))

    min = minutes(birth)
    words = inflect(min)

    print(f'{words} minutes')


def validate(birth):
    regex = r'^(?P<year>\d\d\d\d)-(?P<month>\d\d)-(?P<day>\d\d)$'

    sear = search(regex, birth)
    if not sear:
        exit('Usage: YYYY-MM-DD')

    year = int(sear.group('year'))
    month = int(sear.group('month'))
    day = int(sear.group('day'))

    return year, month, day


def minutes(birth):

    today = date.today()

    current = datetime(today.year, today.month, today.day)
    try:
        inp = datetime(birth[0], birth[1], birth[2])
    except ValueError:
        exit('The date does not exist')

    dif = current - inp

    dif = int(dif.total_seconds() / 60)
    if dif < 0:
        exit('The future didn\'t happen yet!')

    return dif


def inflect(min):
    inf = engine()
    return inf.number_to_words(min, andword='').capitalize()


if __name__ == "__main__":
    main()
