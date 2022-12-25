lines = open('input.txt', 'r').read().splitlines()

digit_map = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}

sum_decimal = sum(digit_map[digit] * 5 ** i for line in lines for i, digit in enumerate(line[::-1]))

sum_snafu = ''

while sum_decimal:
    remainder = sum_decimal % 5
    sum_decimal //= 5

    if remainder <= 2:
        sum_snafu = str(remainder) + sum_snafu
    else:
        sign = '=' if remainder == 3 else '-'
        sum_snafu = sign + sum_snafu
        sum_decimal += 1

print(sum_snafu)
