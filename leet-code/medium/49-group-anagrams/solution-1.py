import tests


# Time O(m*n*log(n))
# Space O(m)
# Where m - len(strs) and n - average(len(current_str))
def group_anagrams(strs):
    anagrams = {}
    for current_str in strs:
        sorted_string = ''.join(sorted(current_str))
        if sorted_string not in anagrams:
            anagrams[sorted_string] = []
        anagrams[sorted_string].append(current_str)
    return list(anagrams.values())


tests.test(group_anagrams)
