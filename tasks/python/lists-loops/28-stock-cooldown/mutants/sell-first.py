def max_trade(prices):
    hold = float('-inf')
    sold = float('-inf')
    rest = 0
    for price in prices[1:]:
        hold, sold, rest = (max(hold, rest - price), hold + price, max(rest, sold))
    return max(0, sold, rest)
