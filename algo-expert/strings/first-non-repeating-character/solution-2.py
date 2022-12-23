import tests


# Time O(n)
# Space O(1) | Because string could contain only lower case latin letter (max 26).
# If the input string could contain any character, then the space complexity would be O(n).
def first_non_repeating_character(string):
    characters = {}
    for i, c in enumerate(string):
        if c not in characters:
            characters[c] = i
            continue
        characters[c] = -1

    for index in characters.values():
        if index != -1:
            return index
    return -1


tests.test(first_non_repeating_character)
