import tests

roman_digits = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


# Time O(n)
# Space O(1)
def roman_to_int(roman: str) -> int:
    last = 0
    result = 0

    for i in range(len(roman)):
        current = roman_digits[roman[i]]
        result += current
        if current > last:
            result -= last * 2
        last = current

    return result


tests.test(roman_to_int)
