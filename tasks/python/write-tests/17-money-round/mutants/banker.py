from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

def rounded_price(text):
    value = Decimal(text).quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)
    if value == 0:
        value = abs(value)
    return format(value, '.2f')
