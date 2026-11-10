import re

def sum_money(values):
    total = 0
    for text in values:
        if not re.fullmatch('-?\\d+\\.\\d{2}', text):
            raise ValueError('money')
        a, b = text.lstrip('-').split('.')
        cents = int(a) * 100 + int(b)
        total += cents
    return ('-' if total < 0 else '') + str(abs(total) // 100) + '.' + f'{abs(total) % 100:02d}'
