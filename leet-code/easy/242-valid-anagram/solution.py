from collections import defaultdict
import tests


# Space O(n)
# Time O(n)
def is_anagram(first: str, second: str) -> bool:
    if len(first) != len(second):
        return False
    characters = defaultdict(int)
    for char in first:
        characters[char] += 1
    for char in second:
        if characters[char] == 0:
            return False
        characters[char] -= 1
    return True


tests.test(is_anagram)
