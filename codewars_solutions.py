# Codewars Solutions Assignment

import math


# Solution: Roman Numerals Encoder
def solution(n):
    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    roman_string = ''
    for key in sorted(roman_numerals.keys(), reverse=True):
        while n >= key:
            roman_string += roman_numerals[key]
            n -= key
    return roman_string


# Solution: Insure an Investment
def insurance_value(S0, T, u, p):
    d = 1 / u
    expected = 0.0

    for k in range(T + 1):
        # Probability of k upward moves
        prob = math.comb(T, k) * (p ** k) * ((1 - p) ** (T - k))

        # Final stock price
        ST = S0 * (u ** k) * (d ** (T - k))

        # Insurance payout
        payoff = max(S0 - ST, 0)
        expected += prob * payoff

    return expected


# Solution: Sum of Digits / Digital Root
def digital_root(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n


# Solution: Product of consecutive Fib numbers
def product_fib(prod):
    a, b = 0, 1
    while a * b < prod:
        a, b = b, a + b
    return [a, b, a * b == prod]
